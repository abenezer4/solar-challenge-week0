# app/utils.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = "data"

def load_data(country: str):
    """Load cleaned CSV for selected country."""
    file_map = {
        "Benin": "benin_clean.csv",
        "Sierra Leone": "sierraleone_clean.csv",
        "Togo": "togo_clean.csv",
    }
    path = f"{DATA_PATH}/{file_map[country]}"
    df = pd.read_csv(path)
    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    return df

def summary_plot(df, cols):
    """Return line plot for selected variables."""
    fig, ax = plt.subplots(figsize=(10, 4))
    for c in cols:
        ax.plot(df["Timestamp"], df[c], label=c)
    ax.set_xlabel("Time")
    ax.legend()
    ax.set_title("Selected Variable Trends Over Time")
    return fig

def correlation_heatmap(df):
    """Return correlation heatmap figure."""
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(df.corr(), annot=True, cmap="YlOrRd", ax=ax)
    ax.set_title("Correlation Heatmap")
    return fig

def ghi_boxplot(df_all):
    """Return boxplot comparing GHI across countries."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="Country", y="GHI", data=df_all, palette="coolwarm", ax=ax)
    ax.set_title("Global Horizontal Irradiance by Country")
    return fig
