import pandas as pd
from sqlalchemy import create_engine, text

def load_to_postgres(df: pd.DataFrame):
    # Ganti sesuai kredensial Anda
    engine = create_engine("postgresql+psycopg2://postgres:yourpassword@localhost:5432/nasa_etl")

    # Pastikan kolom close_approach_date ada
    if 'close_approach_date' not in df.columns:
        raise Exception("Kolom 'close_approach_date' tidak ditemukan di DataFrame")

    # Ambil rentang tanggal dari data
    min_date = df['close_approach_date'].min()
    max_date = df['close_approach_date'].max()

    with engine.begin() as connection:
        # Hapus data dalam rentang tanggal yang akan dimasukkan
        print(f"🧹 Menghapus data asteroid dari {min_date} hingga {max_date}...")
        connection.execute(
            text("""
                DELETE FROM asteroids 
                WHERE close_approach_date BETWEEN :start AND :end
            """),
            {"start": min_date, "end": max_date}
        )

        # Masukkan data baru
        print(f"⬇️  Memasukkan {len(df)} data asteroid...")
        df.to_sql('asteroids', con=connection, if_exists='append', index=False)

    print("✅ Data berhasil dimuat ke database tanpa duplikat.")
