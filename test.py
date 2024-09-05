
import pandas as pd
import plotly.express as px

df = pd.read_csv('bicycle_data.csv')

fig = px.line_map(df, lat="latitud", lon="longitud", color="id", zoom=3, height=900)

fig.update_layout(map_style="open-street-map", map_zoom=4, map_center_lat = 41,
    margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
