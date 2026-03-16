from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os

from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv("GEMINI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="0.1.0",
    description="A Simple API Server for Langchain",
)

add_routes(
    app,
    ChatGoogleGenerativeAI(temperature=0,
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")),
    path="/google",

)

model = ChatGoogleGenerativeAI(
    temperature=0,
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words.")


prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} with 50 words.")

add_routes(
    app,
    prompt1|model,
    path="/essay",
)

add_routes(
    app,
    prompt2|model,
    path="/poem",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

