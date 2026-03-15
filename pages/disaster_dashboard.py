import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.title("🌍 Global Disaster Intelligence Dashboard")

st.markdown("Analyze worldwide disaster events using interactive visual analytics.")

# ------------------------------------------------
# DATA INPUT
# ------------------------------------------------

option = st.radio(
    "Select Data Input Method",
    ["Upload CSV", "Enter Manually"]
)

if option == "Upload CSV":

    file = st.file_uploader("Upload Disaster Data CSV")

    if file:
        data = pd.read_csv(file)

elif option == "Enter Manually":

    st.subheader("Enter Disaster Event")

    disaster = st.selectbox(
        "Disaster Type",
        ["Earthquake","Flood","Wildfire","Cyclone","Tsunami"]
    )

    country = st.text_input("Country")

    lat = st.number_input("Latitude")
    lon = st.number_input("Longitude")

    impact = st.selectbox(
        "Impact Level",
        ["Low","Medium","High"]
    )

    if "disaster_data" not in st.session_state:
        st.session_state.disaster_data = []

    if st.button("Add Event"):

        st.session_state.disaster_data.append({
            "Disaster":disaster,
            "Country":country,
            "Latitude":lat,
            "Longitude":lon,
            "Impact":impact
        })

    data = pd.DataFrame(st.session_state.disaster_data)

# ------------------------------------------------
# VISUALIZATION
# ------------------------------------------------

if 'data' in locals() and not data.empty:

    st.subheader("Disaster Data")

    st.dataframe(data)

    # ------------------------------------------------
    # COLORED DISASTER MAP
    # ------------------------------------------------

    st.subheader("Interactive Disaster Map")

    color_map = {
        "Earthquake":"red",
        "Flood":"blue",
        "Wildfire":"orange",
        "Cyclone":"purple",
        "Tsunami":"green"
    }

    fig = px.scatter_geo(
        data,
        lat="Latitude",
        lon="Longitude",
        color="Disaster",
        hover_name="Country",
        size_max=15,
        color_discrete_map=color_map,
        title="Global Disaster Events"
    )

    fig.update_layout(
        geo=dict(
            showland=True,
            landcolor="rgb(217,217,217)"
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------
    # HEATMAP
    # ------------------------------------------------

    st.subheader("Global Disaster Heatmap")

    heatmap = px.density_mapbox(
        data,
        lat="Latitude",
        lon="Longitude",
        radius=20,
        zoom=1,
        mapbox_style="carto-darkmatter",
        title="Disaster Density Heatmap"
    )

    st.plotly_chart(heatmap, use_container_width=True)

else:

    st.info("Upload data or add disaster events to see analytics.")

# ------------------------------------------------
# LIVE EARTHQUAKE DATA
# ------------------------------------------------

st.divider()

st.subheader("🌎 Live Global Earthquake Data")

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

response = requests.get(url)
data_json = response.json()

earthquakes = []

for event in data_json["features"]:

    place = event["properties"]["place"]
    mag = event["properties"]["mag"]
    coords = event["geometry"]["coordinates"]

    earthquakes.append({
        "Place": place,
        "Magnitude": mag,
        "Longitude": coords[0],
        "Latitude": coords[1]
    })

quake_df = pd.DataFrame(earthquakes)

st.write("Recent earthquakes around the world")

st.dataframe(quake_df)

fig = px.scatter_geo(
    quake_df,
    lat="Latitude",
    lon="Longitude",
    size="Magnitude",
    hover_name="Place",
    color="Magnitude",
    color_continuous_scale="reds",
    title="Live Global Earthquakes"
)

st.plotly_chart(fig, use_container_width=True)