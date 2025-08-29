from google import genai
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
load_dotenv()


# making changes in the existing image using nanobananan
# 1
def UpdateImageNanobanana():
    try:
        nanobanana_api = os.getenv('gemini_nano_banana_apikey')
        client = genai.Client(api_key=nanobanana_api)
        prompt = """
        Create a picture of my dog eating a nano-banana in a fancy restaurant under the gemini constellation
        """
        image = Image.open('mydog.png')

        # Start the generation job
        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents=[prompt, image],
        )

        for part in response.parts:
            if part.text:
                print(part.text)
            elif image := part.as_image():
                image.show()
                image.save("generated_image.png")

    except Exception as e:
        print(e)


UpdateImageNanobanana()


# Generating a new image with nanobanana
# 2
def GenerateImageNanobanana():
    try:
        nanobanana_api = os.getenv('GEMINI_API_KEY')
        client = genai.Client(api_key=nanobanana_api)
        prompt = (
            "Create a picture of a nano banana dish in a fancy restaurant with a Indian Village theme"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents=[prompt],
        )
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                image.save("generated_image.png")
    except Exception as e:
        print(e)


GenerateImageNanobanana()
