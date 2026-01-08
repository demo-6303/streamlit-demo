import streamlit as st
import pandas as pd

st.title("This is my dashboard")

file = st.file_uploader("Upload your file", type = ["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("data preview")
    st.dataframe(df)

    st.subheader("summary")
    st.write(df.describe())

    st.subheader("Filtering data by city")
    cities = df["City"].unique()

    choice  = st.selectbox("Choose your city: ", cities)
    st.dataframe(df[df['City'] == choice])