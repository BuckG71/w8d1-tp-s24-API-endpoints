# Weather App API

This is a simple Weather App API built using Flask that allows users to retrieve current weather information for a specified location. The application fetches data from WeatherAPI.com.

## Assignment Report

My objective was to implement an API that fetches weather data for a specified location and returns it in a structured format. The primary design choice was to ensure the API is easy to use and understand, providing clear and concise responses. I utilized ChatGPT extensively to help with understanding how to implement the API functionalities. The main challenge was integrating the WeatherAPI data with the frontend and ensuring the API handles various error scenarios properly.

## Features

- **Retrieve Weather Information**: Users can fetch current weather data for a specified location.
- **Error Handling**: The API provides meaningful error messages for invalid requests.
- **Structured Data**: The API returns weather data in a structured JSON format.

## Project Structure

``` markdown
weather_app/
├── src/
│   └── …
├── static/
│   └── css/
│       └── …
├── templates/
│   └── …
├── app.py
├── .env
├── .gitignore
└── README.md
```

## Setup Instructions

**Clone the repository:**

``` bash
git clone <your-repo-url>
cd weather_app
```

**Create and activate a virtual environment:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies:**

``` bash
pip install -r requirements.txt
```

**Run the Flask application:**

``` bash
flask run
```

**Instructions to Obtain an API Key from WeatherAPI.com**

1. Visit WeatherAPI.com and sign up for a free account.
2. After signing up, you will receive an API key which you need to use to fetch weather data.
3. Store this API key in your .env file as follows:

``` Python
API_KEY=your_api_key
WEATHER_API_BASE_URL=http://api.weatherapi.com/v1/current.json
TIMEOUT=5
```

## Conclusion

This API provides a straightforward way to retrieve current weather information for a given location using the WeatherAPI.com service. The project structure is designed to be easy to understand and extend.
