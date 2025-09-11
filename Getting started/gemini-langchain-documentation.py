import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
import base64



# Load .env
load_dotenv()
llm = ChatGoogleGenerativeAI(
    temperature=0,
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]

# ai_msg = llm.invoke(messages)
# print("french Translation : ", ai_msg.content)


## chaining - 
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a helpful assistant that translates {input_language} to {output_language}.",
#         ),
#         ("human", "{input}"),
#     ]
# )

# chain = prompt | llm
# ai_msg = chain.invoke(
#     {
#         "input_language": "English",
#         "output_language": "German",
#         "input": "I love programming.",
#     }
# )

# print(ai_msg.content)


## Multimodal Usage - 
## Image Input - 


# Example using a public URL (remains the same)
# message_url = HumanMessage(
#     content=[
#         {
#             "type": "text",
#             "text": "Describe the image at the URL.",
#         },
#         {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
#     ]
# )
# result_url = llm.invoke([message_url])
# print(f"Response for URL image: {result_url.content}")

# Example using a local image file encoded in base64
# image_file_path = r"C:\Users\atalb\Downloads\download.jpg"

# with open(image_file_path, "rb") as image_file:
#     encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# message_local = HumanMessage(
#     content=[
#         {"type": "text", "text": "Describe the local image."},
#         {"type": "image_url", "image_url": f"data:image/png;base64,{encoded_image}"},
#     ]
# )
# result_local = llm.invoke([message_local])
# print(f"Response for local image: {result_local.content}")



## Audio Imput
# Ensure you have an audio file named 'example_audio.mp3' or provide the correct path.
# audio_file_path = r"C:\Users\atalb\Downloads\baby-talk-76380.mp3"
# audio_mime_type = "audio/mpeg"


# with open(audio_file_path, "rb") as audio_file:
#     encoded_audio = base64.b64encode(audio_file.read()).decode("utf-8")

# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "Transcribe the audio."},
#         {
#             "type": "media",
#             "data": encoded_audio,  # Use base64 string directly
#             "mime_type": audio_mime_type,
#         },
#     ]
# )
# response = llm.invoke([message])  # Uncomment to run
# print(f"Response for audio: {response.content}")




## Video Input-  

# # Ensure you have a video file named 'example_video.mp4' or provide the correct path.
# video_file_path = r"C:\Users\atalb\Downloads\sample-5s.mp4"
# video_mime_type = "video/mp4"


# with open(video_file_path, "rb") as video_file:
#     encoded_video = base64.b64encode(video_file.read()).decode("utf-8")

# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "Describe the first few frames of the video."},
#         {
#             "type": "media",
#             "data": encoded_video,  # Use base64 string directly
#             "mime_type": video_mime_type,
#         },
#     ]
# )
# response = llm.invoke([message])  # Uncomment to run
# print(f"Response for video: {response.content}")


import base64

from IPython.display import Image, display
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-preview-image-generation", google_api_key=os.getenv("GEMINI_API_KEY"))

message = {
    "role": "user",
    "content": "Generate a photorealistic image of a cuddly cat wearing a hat.",
}

response = llm.invoke(
    [message],
    generation_config=dict(response_modalities=["TEXT", "IMAGE"]),
)


def _get_image_base64(response: AIMessage) -> None:
    image_block = next(
        block
        for block in response.content
        if isinstance(block, dict) and block.get("image_url")
    )
    return image_block["image_url"].get("url").split(",")[-1]


image_base64 = _get_image_base64(response)
display(Image(data=base64.b64decode(image_base64), width=300))