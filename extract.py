import requests

API_KEY = "yourAPIKEY"  # Ganti dengan API Key NASA-mu kalau ada

def extract_asteroid_data(start_date: str, end_date: str) -> dict:
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}, {response.text}")
    return response.json()
