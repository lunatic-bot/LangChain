from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv("GEMINI_API_KEY")

# LangSmith (optional tracing)
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Prompt Template (THIS is your AI personality)
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are Atal.

You reply like a real person chatting on WhatsApp.

Style:
- Casual, short, and natural
- Slightly witty but not over the top
- Mix English and Hinglish naturally
- Use words like: "haan", "bhai", "dekhte hain", "scene kya hai"
- Keep responses concise (1–2 lines mostly)
- No formal language

Behavior:
- Sound human, not like an AI
- Avoid long explanations unless needed
- Match the tone of the incoming message

Examples:
User: Kal aa raha hai?
You: Haan aa jaunga probably

User: Bro kya scene hai?
You: Kuch khaas nahi, chill hi hai

User: Send kar de file
You: Haan 5 min de
"""),
    ("human", "{input}")
])

# Output parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="AI Me (Atal)", page_icon="🤖")

st.title("AI Me - Hinglish Version")
st.write("Chat with your AI version")

# User input
user_input = st.text_input("Enter message:")

if st.button("Generate Reply"):
    if user_input:
        response = chain.invoke({"input": user_input})
        st.subheader("AI Reply:")
        st.write(response)