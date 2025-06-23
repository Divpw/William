import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Define the OpenRouter API URL
OPENROUTER_API_URL = "https://openrouter.ai/api/v1"

if __name__ == '__main__':
    # This part is for testing purposes and will print the loaded API key
    # and URL when the script is run directly.
    if OPENROUTER_API_KEY:
        print(f"OpenRouter API Key: {OPENROUTER_API_KEY[:5]}... (partially hidden for security)")
    else:
        print("OpenRouter API Key not found. Make sure it's set in the .env file.")
    print(f"OpenRouter API URL: {OPENROUTER_API_URL}")
