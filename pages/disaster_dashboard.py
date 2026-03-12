import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Disaster Monitoring Dashboard")

st.write("Earthquake monitoring using global dataset.")

df = pd.read_csv("data/earthquakes.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

fig = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    size="magnitude",
    zoom=1,
    height=500
)

fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig)