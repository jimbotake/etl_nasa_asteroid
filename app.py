import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from main import run_etl_with_limit
import sqlalchemy
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(page_title="ETL Asteroid NASA", layout="wide")
st.title("🚀 ETL Data Asteroid NASA")
st.markdown("Masukkan rentang waktu maksimum **7 hari** untuk memantau asteroid yang mendekati Bumi.")

# Form input tanggal
with st.form("tanggal_form"):
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Tanggal Mulai", datetime.today() - timedelta(days=2))
    with col2:
        end_date = st.date_input("Tanggal Selesai", datetime.today())
    
    submitted = st.form_submit_button("Jalankan ETL")

# Jalankan ETL saat form disubmit
if submitted:
    # Validasi rentang tanggal
    delta = (end_date - start_date).days
    if delta < 0:
        st.error("❌ Tanggal selesai harus setelah tanggal mulai.")
    elif delta > 7:
        st.error("❌ Rentang tanggal maksimal adalah 7 hari.")
    else:
        try:
            with st.spinner("Mengambil dan memproses data..."):
                run_etl_with_limit(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
            st.success("✅ ETL berhasil dijalankan!")

        except Exception as e:
            st.error(f"Terjadi kesalahan saat menjalankan ETL: {e}")

# Ambil data dari PostgreSQL untuk ditampilkan
try:
    engine = sqlalchemy.create_engine("postgresql://postgres:Humaira31814@localhost:5432/nasa_etl")
    df = pd.read_sql("SELECT * FROM asteroids", engine)

    if not df.empty:
        st.subheader("📋 Data Asteroid")
        st.dataframe(df)

        # Visualisasi interaktif
        st.subheader("📊 Visualisasi Jarak vs Kecepatan Asteroid")

        fig = px.scatter(
            df,
            x="miss_distance_km",
            y="relative_velocity_km_per_sec",
            color="is_potentially_hazardous_asteroid",
            hover_name="name",  # Nama asteroid saat hover
            title="Jarak vs Kecepatan Asteroid",
            labels={
                "miss_distance_km": "Jarak (km)",
                "relative_velocity_km_per_sec": "Kecepatan (km/s)",
                "is_potentially_hazardous_asteroid": "Berbahaya?"
            }
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Belum ada data asteroid di database.")
except Exception as e:
    st.error(f"Gagal mengambil data dari database: {e}")
