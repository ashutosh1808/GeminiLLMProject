from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config("Gemini LLM App")
st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
uploaded_image=st.file_uploader("Choose an image: ",type=["jpg","png","jpeg"])
image=""
submit=st.button("Submit")

if uploaded_image is not None:
    image=Image.open(uploaded_image)
    st.image(image,use_container_width=True,caption='Uploaded image')

if submit:
    response=get_gemini_response(input,image)
    st.header(response)