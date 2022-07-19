import streamlit as st
from PIL import Image


st.markdown(f"<h1 style= font-size:70px;text-align:'center';>Oil Spill Monitoring</h1><br>", unsafe_allow_html=True)
st.image("app\\Untitled (1200 × 768 px) (1300 × 768 px).png", use_column_width=None) 
st.markdown(f"<br><br><h3 style= font-size:50px;>Motivation</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
col1.write("""
###
##### Oil spills happen when fossil fuels are discharged into the ocean due to offshore drilling, fueling transport ships and pipelines.The amount of oil released into the ocean has risen due to the increased aforementioned activity.
- ##### destruction of ecosystems
- ##### loss of animal and human habitat 
- ##### damage to local fishing
- ##### loss to other water based industries.
- ##### health risks due to delay in cleaning as it requires large manpower use of booms and skimmers
""")

image = Image.open("app\image3.png")
col2.image(image, width=600)

st.markdown(f"<hr style=width:100%;text-align:left;margin-left:0;>", unsafe_allow_html=True)

st.markdown(f"<h3 style= font-size:50px;>Our Idea/Solution</h3>", unsafe_allow_html=True)
col3, col4 = st.columns(2)
col4.write("""

#

##### An AI-based model to detect oil spills in the ocean or other bodies of water using satellite imagery.
- ##### Oil spill mapping
- ##### Slick detection and surveillance
- ##### Oil spill movement forecast 
- ##### Potential oil spill prediction 
- ##### Direct support for oil spill countermeasures
- ##### Slick trajectory determination
""")

col3.image("app\image2.png",width= 550)

st.markdown(f"<hr style=width:100%;text-align:left;margin-left:0;>", unsafe_allow_html=True)
st.markdown(f"<br><h3 style= font-size:50px;>Future Scope</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
col1.write("""
#
#
- ##### Model takes input as longitude and latitude, get snip of sentinel imagery, and detects the presence of an oil spill.
- ##### Model autonomously monitoring for oil spills all over the world on a regular basis without any manual input and update the dashboard with all the observations collected and studied in real time 
- ##### webpage in more regional languages
""")

image = Image.open("app\image1.png")
col2.image(image, width=600)



