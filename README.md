
# ☄️ NASA NeoWs ETL & Visualization App

Aplikasi ETL (Extract, Transform, Load) untuk data asteroid dari NASA NeoWs (Near Earth Object Web Service) dengan antarmuka interaktif menggunakan **Streamlit**.

## 🚀 Fitur

- 🔍 Input tanggal pantauan asteroid (maks. rentang 7 hari)
- 🛰️ Ekstraksi data asteroid dari NASA Open API
- 🧮 Transformasi & simpan data ke PostgreSQL
- 📊 Visualisasi interaktif (nama, kecepatan, jarak, diameter, bahaya)
- ♻️ Cek duplikasi data sebelum disimpan

---

## ⚙️ Arsitektur ETL

```
NASA API ➡️ Extract (requests) ➡️ Transform (pandas) ➡️ Load (SQLAlchemy + PostgreSQL)
                                              ⬇️
                                         Streamlit UI
```

---

## 📦 Struktur Proyek

```
etl_nasa/
│
├── app.py                  # Streamlit interface
├── main.py                 # Run ETL pipeline
├── extract.py              # Ambil data dari NASA API
├── transform.py            # Proses data
├── load.py                 # Simpan ke PostgreSQL
├── requirements.txt
└── README.md
```

---

## 💡 Contoh Penggunaan

```bash
# Jalankan ETL + Visualisasi
streamlit run app.py
```

---

## 🔑 API Key NASA

Daftar gratis di [https://api.nasa.gov](https://api.nasa.gov) lalu buat `.env`:

```
NASA_API_KEY=DEMO_KEY
```

---

## 🗄️ Database

Pastikan PostgreSQL aktif dan sesuaikan kredensial di `load.py`. Contoh koneksi:

```python
engine = create_engine('postgresql://postgres:your_password@localhost:5432/nasa_etl')
```

---

## 🧪 Contoh Visualisasi

- **Bar chart**: Asteroid dengan diameter terbesar
- **Bubble chart**: Kecepatan vs Jarak
- **Tabel data mentah**

---

## Tampilan Aplikasi
![Tampilan Aplikasi](images/capture.png)

---

## 🧼 Cegah Duplikasi

ETL akan menghapus asteroid dengan ID yang sama sebelum menyimpan data baru, mencegah duplikasi.

---

## 🧰 Requirements

Install dependency dengan:

```bash
pip install -r requirements.txt
```

---

## 📝 Lisensi

MIT License © 2025
