from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, AIMessage

import streamlit as st
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv("GEMINI_API_KEY")

# LangSmith tracing (optional)
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

# Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Prompt with memory placeholder
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
- Be a little polite but friendly
"""),

    # 👇 THIS is memory
    MessagesPlaceholder(variable_name="chat_history"),

    ("human", "{input}")
])

output_parser = StrOutputParser()
chain = prompt | llm | output_parser


# ---------------- STREAMLIT ---------------- #

st.set_page_config(page_title="AI Me (Atal)", page_icon="🤖")
st.title("AI Me - With Memory")

# Initialize memory in session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input
user_input = st.text_input("Enter message:")

if st.button("Send"):
    if user_input:
        #limit memory
        st.session_state.chat_history = st.session_state.chat_history[-10:]

        # Generate response with memory
        response = chain.invoke({
            "input": user_input,
            "chat_history": st.session_state.chat_history
        })

        # Save to memory
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.session_state.chat_history.append(AIMessage(content=response))

# Display chat
st.subheader("Conversation")

for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.write(f"🧑 You: {msg.content}")
    else:
        st.write(f"🤖 AI: {msg.content}")