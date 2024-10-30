import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd

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
    "api_key": os.getenv("API_KEY")
}

# Define a maximum filename length
MAX_FILENAME_LENGTH = 50

# Truncate the components if needed to ensure the final filename length is within the limit
def truncate_text(text, max_length):
    return text[:max_length] if len(text) > max_length else text

# Make the request to your private API
try:
    response = requests.post(PRIVATE_API_URL, json=params)
    response.raise_for_status()
    data = response.json()

    # Define filename with timestamp, place_type/keyword, and location
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    place_type = truncate_text(params.get("place_type", "unknown"), 15)
    keyword = truncate_text(params.get("keyword", "unknown"), 15)
    location = truncate_text(params.get("location", "unknown").replace(" ", "_"), 20)
    filename = f"data/{timestamp}_{place_type}_{keyword}_{location}.csv"

    # Ensure the filename does not exceed the maximum allowed length
    if len(filename) > MAX_FILENAME_LENGTH:
        filename = filename[:MAX_FILENAME_LENGTH] + ".csv"

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(data.get("results", []))
    os.makedirs("data", exist_ok=True)  # Ensure the 'data' directory exists
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

except requests.exceptions.RequestException as e:
    print("Failed to retrieve data:", e)
