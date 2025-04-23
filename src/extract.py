import requests
import pandas as pd
import logging

def extract_data(start_time="2024-01-01", end_time="2024-12-31", min_magnitude=4.5):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": start_time,
        "endtime": end_time,
        "minmagnitude": min_magnitude
    }
    logging.info(f"Requesting data from USGS API: {params}")
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()["features"]
    records = []
    logging.info(f"Extracted {len(data)} earthquake records")

    for quake in data:
        props = quake["properties"]
        coords = quake["geometry"]["coordinates"]
        records.append({
            "time": props["time"],
            "place": props["place"],
            "mag": props["mag"],
            "longitude": coords[0],
            "latitude": coords[1],
            "depth": coords[2]
        })

    return pd.DataFrame(records)
