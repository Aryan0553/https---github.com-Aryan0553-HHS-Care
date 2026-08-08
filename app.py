import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="HHS Care Forecasting",
    layout="wide"
)

st.title("🏥 HHS Care Forecasting & Capacity Planning")

df = pd.read_excel("HHS_Care_Forecasting.xlsx")

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()

st.sidebar.title("Filters")

year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

month = st.sidebar.selectbox(
    "Select Month",
    sorted(df["Month"].unique())
)

filtered = df[
    df["Year"] == year
]

col1,col2,col3,col4,col5=st.columns(5)

col1.metric(
    "Children in HHS Care",
    int(filtered["Children in HHS Care"].mean())
)

col2.metric(
    "Transfers",
    int(filtered["Children transferred out of CBP custody"].sum())
)

col3.metric(
    "Discharges",
    int(filtered["Children discharged from HHS Care"].sum())
)

col4.metric(
    "Net Pressure",
    int(filtered["Net_Pressure"].mean())
)

col5.metric(
    "High Risk Days",
    len(filtered[
        filtered["Capacity_Risk"]=="High Risk"
    ])
)

fig,ax=plt.subplots(figsize=(12,5))

ax.plot(
filtered["Date"],
filtered["Children in HHS Care"]
)

ax.set_title(
"HHS Care Population Trend"
)

st.pyplot(fig)


st.subheader(
"Dataset"
)

st.dataframe(filtered)

