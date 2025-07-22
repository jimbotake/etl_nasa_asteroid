import pandas as pd

def transform_asteroid_data(raw_data: dict) -> pd.DataFrame:
    asteroids_list = []

    near_earth_objects = raw_data.get('near_earth_objects', {})

    for date, asteroids in near_earth_objects.items():
        for asteroid in asteroids:
            est_diameter = asteroid['estimated_diameter']['meters']
            diameter_min = est_diameter['estimated_diameter_min']
            diameter_max = est_diameter['estimated_diameter_max']
            close_approach_data = asteroid['close_approach_data'][0]

            asteroids_list.append({
                "id": asteroid['id'],
                "name": asteroid['name'],
                "close_approach_date": close_approach_data['close_approach_date'],
                "relative_velocity_km_per_sec": float(close_approach_data['relative_velocity']['kilometers_per_second']),
                "miss_distance_km": float(close_approach_data['miss_distance']['kilometers']),
                "estimated_diameter_min": diameter_min,
                "estimated_diameter_max": diameter_max,
                "is_potentially_hazardous_asteroid": asteroid['is_potentially_hazardous_asteroid']
            })

    df = pd.DataFrame(asteroids_list)
    return df
