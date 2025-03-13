from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

# api = os.getenv("GEMINI_API_KEY")
# user_input = input("Ask a query: ")
# sys_instruct = "you are Arijit Singh"
# client = genai.Client(api_key=api)
# response = client.models.generate_content_stream(
#     model="gemini-2.0-flash",  config=types.GenerateContentConfig(
#         system_instruction=sys_instruct),
#     contents=[user_input]
# )
# for chunk in response:
#     print(chunk.text, end="")


def Gemini_Song_Recomendation(user_query):
    api = os.getenv("GEMINI_API_KEY")
    system_instruction = "You are Arijit Singh"
    client = genai.Client(api_key=api)

    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",  config=types.GenerateContentConfig(
            system_instruction=system_instruction),
        contents=[user_input]
    )
    for chunk in response:
        print(chunk.text, end="")


user_input = input("Ask a query: ")
Gemini_Song_Recomendation(user_query=user_input)
