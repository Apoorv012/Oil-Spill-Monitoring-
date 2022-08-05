import cv2
import os
import streamlit as st
from PIL import Image
from predict import predict_image
from config import view_image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

with st.sidebar:
    choose = option_menu("Gallery", ["Home", "Oil Spills Near me", "Oil Spills Detection"],
                         icons=[],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == 'Home':

    # Page
    st.markdown(f"<h1 style= font-size:70px;text-align:'center';>Oil Spill Monitoring</h1><br>",
                unsafe_allow_html=True)
    st.image(os.path.join("app", "untitled.png"), use_column_width=None)
    st.markdown(f"<br><br><h3 style= font-size:50px;>Motivation</h3>",
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.write("""
    ##### Oil spills happen when fossil fuels are discharged into the ocean due to offshore drilling, fueling transport ships and pipelines.The amount of oil released into the ocean has risen due to the increased aforementioned activity.
    - ##### destruction of ecosystems
    - ##### loss of animal and human habitat 
    - ##### damage to local fishing
    - ##### loss to other water based industries.
    - ##### health risks due to delay in cleaning as it requires large manpower use of booms and skimmers
    """)

    image = Image.open(os.path.join("app", "image1.png"))
    col2.image(image, width=600)

    st.markdown(f"<hr style=width:100%;text-align:left;margin-left:0;>",
                unsafe_allow_html=True)

    st.markdown(f"<h3 style= font-size:50px;>Our Idea/Solution</h3>",
                unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    col4.write("""
    ##### An AI-based model to detect oil spills in the ocean or other bodies of water using satellite imagery.
    - ##### Oil spill mapping
    - ##### Potential oil spill prediction 
    - ##### Direct support for oil spill countermeasures
    """)

    col3.image(os.path.join("app", "image2.png"), width=600)

    st.markdown(f"<hr style=width:100%;text-align:left;margin-left:0;>",
                unsafe_allow_html=True)
    st.markdown(f"<br><h3 style= font-size:50px;>Future Scope</h3>",
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.write("""
    - ##### Model takes input as longitude and latitude, get snip of sentinel imagery, and detects the presence of an oil spill.
    - ##### Model autonomously monitoring for oil spills all over the world on a regular basis without any manual input and update the dashboard with all the observations collected and studied in real time 
    - ##### webpage in more regional languages
    """)

    image = Image.open(os.path.join("app", "image3.png"))
    col2.image(image, width=600)


if choose == 'Oil Spills Near me':
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
            # pitch=50,
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


if choose == 'Oil Spills Detection':
    st.title('Oil Spill')
    st.subheader("Content Image")
    main_image = st.file_uploader(
        "Upload Images", type=["png", "jpg", "jpeg"], key='main_image')

    if main_image is not None:
        file_details = {"filename": main_image.name, "filetype": main_image.type,
                        "filesize": main_image.size}
        st.write(file_details)
        st.image(view_image(main_image), width=400)
        with open(os.path.join("images", main_image.name), "wb") as f:
            f.write((main_image).getbuffer())

    clicked = st.button('Check for oil spill')

    if clicked:
        if main_image is not None:
            predictions = predict_image(
                os.path.join("images", main_image.name))
            st.write('### Output image:')
            st.markdown(predictions, unsafe_allow_html=True)
        else:
            st.write('Please Upload files properly')
