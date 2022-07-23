import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv("incidents (1).csv")

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

req_cols = ["lat", "lon"]
df = df[req_cols]

st.title("Oil Spills Near Me")


st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/satellite-v9',
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=2,
        #pitch=50,
    ),
    layers=[
        # pdk.Layer(
        #     'HexagonLayer',
        #     data=df,
        #     get_position='[lon, lat]',
        #     radius=200,
        #     elevation_scale=4,
        #     elevation_range=[0, 1000],
        #     pickable=True,
        #     extruded=True,
        # ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200000,
        ),
    ],
))
