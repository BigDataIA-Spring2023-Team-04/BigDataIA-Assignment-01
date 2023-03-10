import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

st.title("Next Generation Weather Radar(NEXRAD) Locations")
st.caption("Source: National Oceanic and Atmospheric Administration")


import pandas as pd

# load the data into a pandas dataframe
df = pd.read_csv("nexrad-stations.csv")

m = folium.Map(
    location=[df["LAT"].mean(), df["LON"].mean()],
    width=700,
    height=1000,
    zoom_start=5,
    min_zoom=4,
    no_wrap=True,
    max_bounds=True,
    tiles="OpenStreetMap",
)
# Add markers to the map
for i, row in df.iterrows():
    folium.Marker(
        [row["LAT"], row["LON"]],
        tooltip=f"Station Name: {row['NAME']}<br>Station ID: {row['ICAO']}<br>Country: {row['COUNTRY']}<br>State: {row['ST']}<br>County: {row['COUNTY']}<br>Latitude: {row['LAT']:.4f}<br>Longitude: {row['LON']:.4f}",
    ).add_to(m)


# Add the map to the Streamlit app
st_data = st_folium(m, width=700)

st.metric(label="Total NEXRAD Stations :", value=df["NAME"].count())
