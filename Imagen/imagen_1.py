
# Generate Model using Google's Imagen

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os
load_dotenv()


def GenerateImageImagen():
    try:
        imagen_apiKey = os.getenv('GEMINI_API_KEY')
        client = genai.Client(api_key=imagen_apiKey)
        response = client.models.generate_images(
            model='imagen-4.0-generate-001',
            prompt='A Dog doing skydiving',
            config=types.GenerateImagesConfig(number_of_images=1,)
        )

        for generateImage in response.generated_images:
            generateImage.image.show()

    except Exception as e:
        print(e)


GenerateImageImagen()
