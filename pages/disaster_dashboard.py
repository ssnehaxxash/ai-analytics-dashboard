import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Disaster Monitoring Dashboard")

# -----------------------------
# Session Storage
# -----------------------------

if "disaster_data" not in st.session_state:
    st.session_state.disaster_data = pd.DataFrame(
        columns=["Disaster","Country","Year","Deaths"]
    )

# -----------------------------
# Add Disaster Form
# -----------------------------

st.subheader("Add Disaster Record")

col1, col2 = st.columns(2)

with col1:
    disaster = st.text_input("Disaster Type")

with col2:
    country = st.text_input("Country")

col3, col4 = st.columns(2)

with col3:
    year = st.number_input("Year", min_value=1900, max_value=2100, step=1)

with col4:
    deaths = st.number_input("Deaths", min_value=0)

if st.button("Add Disaster"):

    new_row = pd.DataFrame({
        "Disaster":[disaster],
        "Country":[country],
        "Year":[year],
        "Deaths":[deaths]
    })

    st.session_state.disaster_data = pd.concat(
        [st.session_state.disaster_data, new_row],
        ignore_index=True
    )

    st.success("Disaster added successfully")

# -----------------------------
# Display Table
# -----------------------------

df = st.session_state.disaster_data

st.subheader("Disaster Records")

st.dataframe(df, use_container_width=True)

# -----------------------------
# Analytics
# -----------------------------

if len(df) > 0:

    st.subheader("Disaster Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Events", len(df))
    col2.metric("Countries Affected", df["Country"].nunique())
    col3.metric("Total Deaths", int(df["Deaths"].sum()))

    fig = px.bar(
        df,
        x="Country",
        y="Deaths",
        color="Disaster",
        title="Disaster Impact by Country"
    )

    st.plotly_chart(fig, use_container_width=True)