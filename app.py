import streamlit as st
import pandas as pd
import numpy as np
from geopy.distance import geodesic
import pydeck as pdk

# Page config
st.set_page_config(page_title="Uber Pickup Distance from Times Square", layout="wide")

# Title
st.title("🚖 Uber Pickup Distance from Times Square")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("uber-raw-data-apr14.csv")
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df['lat'] = df['Lat']
    df['lon'] = df['Lon']
    return df

df = load_data()

# Times Square coordinates
TIMES_SQUARE = (40.7580, -73.9855)

# Calculate distance from Times Square
def calc_distance(row):
    return geodesic((row['lat'], row['lon']), TIMES_SQUARE).km

df['distance_from_TS_km'] = df.apply(calc_distance, axis=1)

# Show data preview
st.subheader("📄 Data Preview")
st.dataframe(df[['Date/Time', 'lat', 'lon', 'Base', 'distance_from_TS_km']].head())

# Map of pickups
st.subheader("🗺️ Pickup Locations on Map")
st.map(df[['lat', 'lon']])

# Distance histogram
st.subheader("📏 Distribution of Pickup Distances from Times Square")
st.bar_chart(np.histogram(df['distance_from_TS_km'], bins=20)[0])

# Pickups by Base
st.subheader("📊 Number of Pickups by Base")
st.bar_chart(df['Base'].value_counts())

# Pickups by Hour
st.subheader("⏰ Number of Pickups by Hour")
df['Hour'] = df['Date/Time'].dt.hour
hourly_pickups = df.groupby('Hour').size()
st.line_chart(hourly_pickups)

