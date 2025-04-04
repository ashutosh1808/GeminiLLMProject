from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config("Gemini LLM App")
st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Submit")

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)
