const locationButton = document.getElementById('locationButton');
const locationInput = document.getElementById('location');

locationButton.addEventListener('click', () => {
	const locationValue = locationInput.value.trim();

	if (locationValue) { 
        // Prepare data to send by converting the locationValue into JSON format
        const dataToSend = JSON.stringify({ locationValue });

        // Use the fetch API to make a POST request to the server with the location data
        fetch('/location', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: dataToSend 
        })
        .then(response => response.json()) 
        .then(data => {
            // Update the current weather information
            document.getElementById('current-weather').innerHTML = data.current_data;
            // Update the hourly forecast
            document.getElementById('hourly-forecast').innerHTML = data.hourly_data;
            // Update the 5-day forecast
            document.getElementById('5-day-forecast').innerHTML = data.day5_data;
        })
        .catch(error => console.error('Error:', error));
    }
});

locationInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter')
        locationButton.click();
});
