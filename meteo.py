import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template

# Carica le variabili da .env
load_dotenv()

app = Flask(__name__)

# API key for WeatherAPI
API_KEY = os.getenv("API_KEY")

@app.route('/')
def render():
    return render_template('index.html')

# Endpoint to handle location data sent from the client and return weather data
@app.route('/location', methods=['POST'])
def get_location():
    # Get the location value from the JSON data in the POST request
    location = request.get_json().get('locationValue')
    # Call get_data() to retrieve current, hourly, and 5-day weather data for the location
    current_data, hourly_data, day5_data = get_data(location)
    # Return the data as JSON to the client
    return jsonify(current_data=current_data, hourly_data=hourly_data, day5_data=day5_data) 

def get_data(location):
    try:
        # Construct the API URL for a 5-day forecast
        url = f'https://api.weatherapi.com/v1/forecast.json?key={weatherAPIKey}&q={location}&days=5'
        
        # Make the request to WeatherAPI and parse the response as JSON
        data = requests.get(url).json()
        
        # Generate HTML segments for current, hourly, and 5-day forecasts
        current_data = current(data)
        hourly_data = hourly(data)
        day5_data = day5(data)
        
        return current_data, hourly_data, day5_data
    except Exception as e:
        print("Unexpected error:", e)
        return "Error", "Error", "Error"

# Function to format current weather data as HTML
def current(data):  
    # Extract relevant weather details from the API response
    temperature = data['current']['temp_c']
    feelslike = data['current']['feelslike_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']
    sunrise = data['forecast']['forecastday'][0]['astro']['sunrise']
    sunset = data['forecast']['forecastday'][0]['astro']['sunset']
    
    # Create an HTML string with the current weather data
    current_html = f"""
        <p>Temperature: {temperature}°C</p>
        <p>Feels like temperature: {feelslike}°C</p>
        <p>Condition: {condition}</p>
        <p>Humidity: {humidity}%</p>
        <p>Sunrise: {sunrise}</p>
        <p>Sunset: {sunset}</p>
    """
    return current_html

# Function to format hourly forecast data as HTML
def hourly(data):
    hourly_forecast = data['forecast']['forecastday'][0]['hour'] 
    hourly_html = ""

    # Loop through each hour to build the HTML for each time slot
    for hour in hourly_forecast:
        time = hour['time']
        temp = hour['temp_c']
        humidity = hour['humidity']
        condition = hour['condition']['text']
        hourly_html += f"<p>{time} temperature is {temp}°C with {humidity}% humidity and {condition.lower()} sky</p>"
    
    return hourly_html

# Function to format 5-day forecast data as HTML
def day5(data):
    day5_forecast = data['forecast']['forecastday']
    day5_html = ""

    # Loop through each day to build the HTML for each day's forecast
    for day in day5_forecast:
        date = day['date']
        max_temp = day['day']['maxtemp_c']
        min_temp = day['day']['mintemp_c']
        humidity = day['day']['avghumidity']
        condition = day['day']['condition']['text']
        day5_html += f"<p>{date}: Highest temperature: {max_temp}°C, lowest temperature: {min_temp}°C with {humidity}% humidity and {condition.lower()} sky.</p>"
    return day5_html

if __name__ == "__main__":
    app.run(port=5000, debug=True)
