import streamlit as st
import pandas as pd

df = pd.read_csv("approved_beneficiaries.csv")

st.title("Senior Citizen Welfare Dashboard")
st.metric("Total Approved", len(df))

lga_counts = df["lga"].value_counts()
st.bar_chart(lga_counts)
