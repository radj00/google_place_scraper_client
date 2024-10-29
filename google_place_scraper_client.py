import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API URL for accessing the private repository's endpoint
PRIVATE_API_URL = os.getenv("API_URL")

# Set parameters for the private API request
params = {
    "lat_and_long": os.getenv("LAT_AND_LONG"),  # e.g., "37.7749,-122.4194"
    "radius": os.getenv("RADIUS"),              # e.g., "1000"
    "location": os.getenv("LOCATION"),          # e.g., "San Francisco, CA"
    "place_type": os.getenv("PLACE_TYPE"),      # e.g., "restaurant"
    "keyword": os.getenv("KEYWORD", ""),        # Default to an empty string if not provided
    "api_key": os.getenv("API_KEY")             # Your API key
}

# Make the request to your private API
try:
    response = requests.post(PRIVATE_API_URL, json=params)
    response.raise_for_status()
    data = response.json()
    print("Data received from private API:", data)

except requests.exceptions.HTTPError as err:
    print(f"Failed to retrieve data: {err}")
    print(f"Response content: {response.text}")  # This will show the error message from the API

except requests.exceptions.RequestException as e:
    print("Failed to retrieve data:", e)
