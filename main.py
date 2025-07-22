from extract import extract_asteroid_data
from transform import transform_asteroid_data
from load import load_to_postgres
from datetime import datetime, timedelta

def run_etl_with_limit(start_date: str, end_date: str):
    print("🚀 Menjalankan ETL NASA NeoWs dengan batch 7 hari...")
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    max_range = timedelta(days=7)
    
    current_start = start_dt
    while current_start <= end_dt:
        current_end = min(current_start + max_range - timedelta(days=1), end_dt)
        print(f"📅 Memproses data dari {current_start.date()} sampai {current_end.date()}")
        raw_data = extract_asteroid_data(current_start.strftime("%Y-%m-%d"), current_end.strftime("%Y-%m-%d"))
        print("✅ Data berhasil diambil")
        df = transform_asteroid_data(raw_data)
        print(f"📊 Jumlah asteroid: {len(df)}")
        load_to_postgres(df)
        current_start = current_end + timedelta(days=1)
    print("🎯 ETL selesai!")

if __name__ == "__main__":
    # Contoh panggilan
    run_etl_with_limit("2025-07-01", "2025-07-22")
