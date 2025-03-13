from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()


def Gemini_recomendation(user_input):
    gemini_instructions = "Think and Act like Elon Musk"

    api = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api)
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",  config=types.GenerateContentConfig(
            system_instruction=gemini_instructions),
        contents=[user_input])

    for chunk in response:
        print(chunk.text, end="")


user_input = input("Ask Query:")
Gemini_recomendation(user_input=user_input)
