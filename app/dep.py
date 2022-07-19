# Import Modules
import streamlit as st
from keras.models import load_model
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np
import os

CATEGORIES = ['No oil spill', 'Oil spill']

# Functions
@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('model-0.52.h5')
  return model

with st.spinner('Model is being loaded..'):
  model=load_model()

def import_and_predict(image_data, model):
    global CATEGORIES
    img = np.asarray(image_data)
    new_arr = cv2.resize(img, (60, 60))
    new_arr = np.array(new_arr)
    new_arr = new_arr.reshape(-1, 60, 60, 1)
    prediction1 = model.predict([new_arr])
    prediction = CATEGORIES[prediction1.argmax()]
    print("Luna=",prediction1)
    return prediction

def load_list_of_images_available(path):
    return os.listdir(path)           


# Main Code

if __name__ == "__main__":
    model = load_model()

    st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

    st.markdown(f"<h1 style= font-size:70px;text-align:'center';>Oil Spill Detection</h1><br>", unsafe_allow_html=True)
    st.image("Untitled (1200 × 768 px) (1300 × 768 px).png", use_column_width=None) 

    st.markdown(f"<hr style=width:100%;text-align:left;margin-left:0;>", unsafe_allow_html=True)

    st.markdown(f"<h3 style= font-size:50px;>Problem Statement</h3>", unsafe_allow_html=True)
    problem ="""Oil spills can contaminate water sources and kill plants and animals, which may lead to further problems in the long-term.
     The most effective way to avoid disasters of this kind is by dealing with them promptly before they spread too much. 
     There are currently no effective means for detecting oil spills in the ocean. Current methods of spotting spills such as aerial surveys are costly and time consuming."""

    st.write(problem)
    st.markdown(f"<hr style=width:100%;text-align:left;margin-left:0;>", unsafe_allow_html=True)


    instructions = """
        Either upload your own image or select from
        the sidebar to get a preconfigured image.
        The image you select or upload will be fed
        through the Deep Neural Network in real-time
        and the output will be displayed to the screen.
        """
    st.write(instructions)

   
    file = st.file_uploader('Upload An Image')
    dtype_file_structure_mapping = {
        'Training Folder': 'train',
        # 'Images Used To Train The Model': 'train',
        'Validation Folder': 'val'
        # 'Images The Model Has Never Seen': 'val'
    }
    data_split_names = list(dtype_file_structure_mapping.keys())
    category_mapping = {
        "Oil Spill": "oil spill",
        "No Oil Spill": "no oil spill"
    }
    category_names = category_mapping.keys()

    

    if file:
        
        image = Image.open(file)
        st.image(image, use_column_width=True)
        predictions = import_and_predict(image, model)
        ttd = str(predictions)+ " detected."
        st.markdown(f"<h4 style='text-align: center; '>{ttd}</h4>", unsafe_allow_html=True)
        #st.header(ttd)
        
    else :
        
        dataset_type = st.sidebar.selectbox("Data Portion Type", data_split_names)
        image_files_subset = dtype_file_structure_mapping[dataset_type]

        selected_category = st.sidebar.selectbox("Oil Spill", category_names)
        category_subset = category_mapping[selected_category]
        path = os.path.join("OIL SPILL", image_files_subset, category_subset)
        image_lists = st.sidebar.selectbox("Image Name", load_list_of_images_available(path))
        image_path =os.path.join(path, image_lists)

        if st.sidebar.button("enter"):
            image = Image.open(image_path)
            st.image(image, use_column_width=True)
            predictions = import_and_predict(image, model)
            ttd = str(predictions)+ " detected."
            st.markdown(f"<h4 style='text-align: center; '>{ttd}</h4>", unsafe_allow_html=True)
            #st.header(ttd)

        else:
            pass


        st.markdown ('<style>button.css-1qrvfrg edgvbvh9{display: flex;  justify-content: center;  align-items: center;}</style>',unsafe_allow_html=True)


        
