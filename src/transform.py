import pandas as pd
import logging
from datetime import datetime

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting data transformation")

    # Convert timestamp to datetime
    df["time"] = pd.to_datetime(df["time"], unit="ms", errors="coerce")

    # Drop rows with missing values
    df.dropna(subset=["time", "mag", "latitude", "longitude", "depth", "place"], inplace=True)

    # Extract region from 'place' field (take the part after the comma)
    # Place is 80 km NW of Kandrian, Papua New Guinea so region will be Papua New Guinea
    df["region"] = df["place"].apply(lambda x: x.split(",")[-1].strip() if "," in x else "Unknown")

    # Create magnitude category
    def categorize_magnitude(mag):
        if mag < 4.0:
            return "Minor"
        elif mag < 5.0:
            return "Light"
        elif mag < 6.0:
            return "Moderate"
        elif mag < 7.0:
            return "Strong"
        else:
            return "Major"

    df["mag_category"] = df["mag"].apply(categorize_magnitude)

    # Extract date parts for time-series analysis
    df["year"] = df["time"].dt.year
    df["month"] = df["time"].dt.month
    df["day"] = df["time"].dt.day

    # Normalize depth
    depth_min = df["depth"].min()
    depth_max = df["depth"].max()
    df["depth_normalized"] = (df["depth"] - depth_min) / (depth_max - depth_min)

    logging.info("Transformation complete")
    return df
