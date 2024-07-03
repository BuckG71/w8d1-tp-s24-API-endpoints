from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('WEATHER_API_BASE_URL')
TIMEOUT = int(os.getenv('TIMEOUT', 5))

# Initialize the Flask application
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})  # Enable CORS for all routes

@app.route('/weather', methods=['GET'])
def get_weather():
    query = request.args.get('query')
    print(f"Received query: {query}")  # Debug print statement
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    params = {
        'key': API_KEY,
        'q': query
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        print(f"Weather API response: {response.json()}")  # Debug print statement
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Weather API: {e}")  # Debug print statement
        return jsonify({'error': str(e)}), 500

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data.get('location', {}).get('name'),
            'temperature': data.get('current', {}).get('temp_f'),
            'condition': data.get('current', {}).get('condition', {}).get('text'),
            'humidity': data.get('current', {}).get('humidity'),
            'wind_speed': data.get('current', {}).get('wind_mph')
        }
        print(f"Weather data: {weather_data}")  # Debug print statement
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)