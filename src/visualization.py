# src/visualize.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_visuals(df: pd.DataFrame):
    # Distribution of Magnitudes
    plt.figure(figsize=(8, 4))
    sns.histplot(df["mag"], bins=30, kde=True)
    plt.title("Distribution of Earthquake Magnitudes")
    plt.xlabel("Magnitude")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("data/magnitude_distribution.png")

    # Time Series: Earthquakes per Month
    df['month_str'] = df['time'].dt.to_period("M").astype(str)
    monthly = df.groupby("month_str").size().reset_index(name="count")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=monthly, x="month_str", y="count", marker="o")
    plt.xticks(rotation=45)
    plt.title("Monthly Earthquake Occurrences")
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("data/monthly_earthquakes.png")
