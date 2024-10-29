# Google Place Scraper Client

Welcome to the Google Place Scraper Client! This project provides a simple interface to access and interact with the [radj_google_places_api_scraper](https://github.com/radj00/google_places_api_scraper) through a Flask web service. The client allows users to fetch information about various places based on geographical coordinates and specified parameters.

## Features

- Fetch details about places using latitude and longitude.
- Support for filtering results based on keywords, types, and radius.
- Returns data in a structured JSON format.

## Getting Started

### Prerequisites

- requests>=2.25.1
- python-dotenv>=0.19.0
- Other dependencies as listed in `requirements.txt`

### Installation

1. Clone the repository:

```bash
   git clone https://github.com/radj00/google_place_scraper_client.git
   cd google_place_scraper_client
```

2. Install the required packages:

```bash
    pip install -r requirements.txt
```

3. Set up your environment variables. Create a .env file in the root directory with the following content:

    ```
    LAT_AND_LONG=latitude,longitude
    PLACE_TYPE=desired_place_type
    RADIUS=desired_radius_in_meters
    KEYWORD=optional_keyword_for_search
    LOCATION=city_or_region
    API_KEY=your_google_api_key
    API_URL=https://github.com/radj00/google_places_api_scraper
    ```

## Running the Application
To start the Flask application, run:

```bash
    python google_place_scraper_client.py
```

By default, the application will be available at `https://googleplacesapiscraper-production.up.railway.app/api/fetch_places`.

### Making Requests

You can make a POST request to the `/api/fetch_places` endpoint with the required parameters. For example, you can use Postman or curl:

```bash
    curl -X POST https://googleplacesapiscraper-production.up.railway.app/api/fetch_places/ \
    -H "Content-Type: application/json" \
    -d '{
        "lat_and_long": "latitude,longitude",
        "radius": 1000,
        "location": "location_name",
        "place_type": "place_type",
        "keyword": "search_keyword"
    }'
```

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the LICENSE file for more details.

## Contributing
If you would like to contribute to this project, feel free to open an issue or submit a pull request.

### Key Changes
- Updated the `.env` section to reflect the exact environment variables you listed.
- Ensured that the instructions are clear and correspond to your setup requirements.

Feel free to modify any section further to better fit your project's needs!
