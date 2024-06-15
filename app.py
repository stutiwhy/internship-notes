import streamlit as st
import pandas as pd
from PIL import Image
import base64
import matplotlib.pyplot as plt

def streaml():
    st.title("WHAT")
    st.header("Streamlit")
    st.subheader("Hello, Stuti.")
    st.write("Namaste")
    st.write(7)
    st.markdown("_italia_ __what i am not__")
    st.markdown("""
    | 1 | 2 |
    |---|---|
    | a | b |
    | c | d |
    """)
    st.write(pd.DataFrame({'A' : [1,2,3,4], 'B' : [5,6,7,8]}))
    st.code("print('Hello, World!')")
    b = st.button("DO NOT CLICK !!!")
    if b:
        st.write("WHAT DID I TELL YOU ?!")
    s = st.checkbox("check this :)")
    if s:
        st.write("hacked.")

st.sidebar.title("not a sidebar")

s = st.sidebar.selectbox('select', {1 : 'one', 2 : 'two', 3 : 'three', 69 : 'sixty-nine'})

def visualize():
    u = st.file_uploader("Upload file : ", type = ["jpeg", "pdf", "png"])

    b1 = st.button("Click to show uploaded image.")
    if b1:
        if u is not None:
            image = Image.open(u)
            st.image(image, caption = "is this.. a gate..?", use_column_width = True)
            st.write("Image uploaded successfully.")
        else:
            st.write("Please upload an image.")

    data = {
        'A' : [5,2,7,3,8,4,9,6,2,6],
        'B' : [56,23,49,54,72,94,77,40,36,22]
    }
    df = pd.DataFrame(data)
    st.write("Sample DataFrame : ")
    st.dataframe(df)

    plt.figure(figsize = (10, 5))
    plt.hist(df['A'], bins = 5, alpha = 0.75)
    plt.title('Histogram of Column A')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    st.pyplot(plt)

if s == 1:
    streaml()
elif s == 2:
    visualize()
elif s == 3:
    st.write('what are you doing man.')
elif s == 69:
    st.write("sixty ni-- what?")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
        print(base64.b64encode(data).decode())
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('BG3_CityReveal_01.png')