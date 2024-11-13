import os
from dotenv import load_dotenv

def load_config():
    return load_dotenv()

def get_google_api_key():
    return os.getenv('GOOGLE_API_KEY')