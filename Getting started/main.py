import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env
load_dotenv()

# Initialize LangChain LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.8,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Streamlit app
st.title("LangChain Demo With Gemini API")
input_text = st.text_input("Search the topic you want")

if input_text:
    response = llm.invoke(input_text)   # LangChain API
    st.write(response.content)
