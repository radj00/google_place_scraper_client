import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API URL for accessing the private repository's endpoint
PRIVATE_API_URL = os.getenv("API_URL")

# Set parameters for the private API request
params = {
    "lat_and_long": os.getenv("LAT_AND_LONG"),
    "radius": os.getenv("RADIUS"),
    "location": os.getenv("LOCATION"),
    "place_type": os.getenv("PLACE_TYPE"),
    "keyword": os.getenv("KEYWORD"),
    "api_key": os.getenv("API_KEY")  # Use if needed by Google API directly
}

# Make the request to your private API
try:
    response = requests.post(PRIVATE_API_URL, json=params)
    response.raise_for_status()
    data = response.json()
    print("Data received from private API:", data)

except requests.exceptions.RequestException as e:
    print("Failed to retrieve data:", e)
