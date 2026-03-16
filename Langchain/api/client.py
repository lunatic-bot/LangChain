import requests
import streamlit as st

def get_gemini_response(input_text, router):
    route = f"http://localhost:8000/{router}/invoke"
    response=requests.post(route,json={"input":{'topic':input_text}})

    return response.json()["output"]['content']

st.title("Langchain Demo with GeminiAPI")
input_text = st.text_input("Write the topic you want to geenrate the poem or essay about")

if input_text:
    st.write(get_gemini_response(input_text,"essay"))

# input_text2 = st.text_input("Write the topic you want to geenrate the poem or essay about")

# if input_text2:
#     # st.write(get_gemini_response(input_text2,"poem"))
#     st.write(get_gemini_response(input_text2,"essay"))