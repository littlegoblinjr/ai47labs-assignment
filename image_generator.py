from openai import OpenAI
import base64
from dotenv import load_dotenv
import os
import requests
load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def generate_image(prompt, filename):
    print(f"Generating Image for: {prompt}")
    
    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1536",
            quality="low",
            n=1
        )

        # Check for both formats in case the server defaults to one or the other
        img_obj = response.data[0]
        if hasattr(img_obj, 'b64_json') and img_obj.b64_json:
            print("Received image via Base64.")
            image_data = base64.b64decode(img_obj.b64_json)
        elif hasattr(img_obj, 'url') and img_obj.url:
            print(f"Received image via URL.")
            image_data = requests.get(img_obj.url).content
        else:
            print("Error: No image data (URL or Base64) found in response.")
            return None

        with open(filename, "wb") as f:
            f.write(image_data) 
        
        return filename

    except Exception as e:
        print(f"Image generation failed: {e}")
        return None