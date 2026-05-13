
from dotenv import load_dotenv
import os 
import requests
load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

def get_omdb_metadata(imdb_id):

    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data
    