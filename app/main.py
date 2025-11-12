# app/main.py
import streamlit as st
import pandas as pd
from utils import load_data, summary_plot, correlation_heatmap, ghi_boxplot

st.set_page_config(
    page_title="Solar Data Discovery Dashboard",
  
    layout="wide",
)

st.title("Solar Data Discovery Dashboard")
st.markdown("""
Explore solar irradiance and temperature data across **Benin**, **Sierra Leone**, and **Togo**.  
Use the sidebar controls to interact with the data and visualize patterns dynamically.
""")


countries = ["Benin", "Sierra Leone", "Togo"]
country = st.sidebar.selectbox(" Select Country", countries)


df = load_data(country)
st.subheader(f"{country} — Data Overview")
st.write(df.head())


numeric_cols = [c for c in df.columns if df[c].dtype in ['float64', 'int64'] and c != "Unnamed: 0"]


st.sidebar.header("Visualization Controls")
selected_cols = st.sidebar.multiselect(
    "Select variables to visualize:",
    numeric_cols,
    default=["GHI", "Tamb"]
)


with st.expander("Summary Statistics"):
    st.dataframe(df.describe().T.style.background_gradient(cmap="Blues"))


st.markdown("###  Time Series Trends")
if selected_cols:
    fig = summary_plot(df, selected_cols)
    st.pyplot(fig)


st.markdown("###  Correlation Heatmap")
fig = correlation_heatmap(df[numeric_cols])
st.pyplot(fig)


@st.cache_data
def load_all_countries():
    all_df = []
    for c in countries:
        temp = load_data(c)
        temp["Country"] = c
        all_df.append(temp)
    return pd.concat(all_df, ignore_index=True)

st.markdown("###  Cross-Country Comparison")
df_all = load_all_countries()
fig = ghi_boxplot(df_all)
st.pyplot(fig)

st.markdown("---")
st.markdown("Developed by **Abenezer Sileshi** | 10 Academy Week 0 Challenge 2025")
