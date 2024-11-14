# Weather Forecast Web Application

This project is a web application that provides weather forecasts for a user-specified location. The application offers three types of forecasts: current weather, an hourly forecast, and a 5-day forecast. It is designed with a user-friendly interface using HTML, Bootstrap for styling, and JavaScript to handle user input and manage data retrieval from the backend.

## Features

- **Current Weather**: Displays the current weather conditions for the selected location.
- **Hourly Forecast**: Provides weather predictions for the next few hours.
- **5-Day Forecast**: Shows the weather forecast over the next five days.
- **Responsive UI**: Built with Bootstrap, the application is responsive and accessible on various devices.
- **Location-based Search**: Users can search by entering a location name, which triggers a backend request to retrieve relevant weather data.

## Project Main Files

- ```templates/index.html```: Defines the structure of the main page, including input fields for location, sections to display current weather, hourly, and 5-day forecasts.
- ```static/js/meteo-req.js```: Contains the JavaScript logic to handle user interactions, send data to the backend, and update the webpage with the received forecast data.
- ```meteo.py```: A Python-based backend (not provided here) receives location data from the frontend, fetches weather information from an API, and returns it in JSON format.

## Setup and Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/valeriodesiati/meteo-app.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd meteo-app
   ```
3. **Use Docker Compose**:
   - Ensure you have `Docker` and `Docker Compose` installed and run
    ```bash
     docker-compose up
     ```
4. **Access the app**:
     ```bash
     http://127.0.0.1/5000
     ```

## Usage Instructions

1. **Enter Location**: Type a location name in the search bar.
2. **Get Forecast**: Click the "Get Forecast" button or press Enter. The application will retrieve and display the current, hourly, and 5-day forecasts.


## License

See the [LICENSE](LICENSE) file for details.

## Author

Valerio Desiati
