from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv("GEMINI_API_KEY")
##langsmith tracking
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")


## prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistent. Your job is to respose to user queries"),
        ("user", "Question{question}")
    ]
)

## Streamlit framework
st.title("Langchain Demo with GeminiAPI")
input_text = st.text_input("Search the topic you want to search")

## Gemini LLM
llm = ChatGoogleGenerativeAI(
    temperature=0,
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

