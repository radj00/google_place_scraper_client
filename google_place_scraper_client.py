import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd

# Load environment variables from .env file
load_dotenv()  # Ensure this line is present

# Directly use the environment variable for the API URL
PRIVATE_API_URL = os.getenv("API_URL")  # Use getenv to avoid KeyError

# Check if the API_URL was loaded successfully
if PRIVATE_API_URL is None:
    print("Error: API_URL environment variable is not set.")
    exit(1)  # Exit the script if API_URL is not set

# Set parameters for the private API request
params = {
    "lat_and_long": os.getenv("LAT_AND_LONG"),
    "radius": os.getenv("RADIUS"),
    "location": os.getenv("LOCATION"),
    "place_type": os.getenv("PLACE_TYPE"),
    "keyword": os.getenv("KEYWORD"),
    "api_key": os.getenv("API_KEY")
}

# Make the request to your private API
try:
    response = requests.post(PRIVATE_API_URL, json=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()  # Parse the response JSON
    print("Data retrieved:", data)

    # Filename setup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/{timestamp}_places.csv"

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(data.get("results", []))
    os.makedirs("data", exist_ok=True)  # Ensure the 'data' directory exists
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

except KeyError as ke:
    print(f"Missing environment variable: {ke}")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err} - {response.text}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print("Failed to retrieve data:", e)
