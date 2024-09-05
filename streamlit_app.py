import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Bicycle Data Visualization", layout="wide")

# Title
st.title("Fuenlabrada")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('bicycle_data.csv')

df = load_data()

# Sidebar for data selection
st.sidebar.header("Data Selection")
selected_ids = st.sidebar.multiselect("Select Bicycle IDs", options=df['id'].unique(), default=df['id'].unique())

# Filter data based on selection
filtered_df = df[df['id'].isin(selected_ids)]

# Map
st.header("Bicycle Locations")
fig = px.line_mapbox(filtered_df, lat="latitud", lon="longitud", color="id", zoom=3, height=600)
fig.update_layout(
    mapbox_style="open-street-map", 
    mapbox_zoom=4, 
    mapbox_center_lat=41,
    margin={"r":0,"t":0,"l":0,"b":0}
)
st.plotly_chart(fig, use_container_width=True)

# Statistics
st.header("Statistics")

# Combine all statistics into a single DataFrame
stats_df = filtered_df.groupby('id').agg({
    'bateria': 'mean',
    'cobertura': 'mean',
    'total_distance': 'first'
}).reset_index()

stats_df.columns = ['ID', 'Average Battery', 'Average Coverage', 'Total Distance']

# Round the numeric columns to 2 decimal places
stats_df['Average Battery'] = stats_df['Average Battery'].round(2)
stats_df['Average Coverage'] = stats_df['Average Coverage'].round(2)
stats_df['Total Distance'] = stats_df['Total Distance'].round(2)

# Display the combined statistics table
st.dataframe(stats_df, use_container_width=True)

# Optional: Add a download button for the statistics
csv = stats_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download statistics as CSV",
    data=csv,
    file_name="bicycle_statistics.csv",
    mime="text/csv",
)

# Download links
st.header("Download Data")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name="filtered_bicycle_data.csv",
    mime="text/csv",
)