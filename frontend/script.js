document.getElementById('weather-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const query = document.getElementById('query').value;
    const weatherResult = document.getElementById('weather-result');
    
    weatherResult.innerHTML = '<p>Loading...</p>';
    
    const url = `http://127.0.0.1:5000/weather?query=${query}`;  
    
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Data:', data);  // Debugging: log the data received from the API
            
            if (data.error) {
                weatherResult.innerHTML = `<p>${data.error}</p>`;
            } else {
                weatherResult.innerHTML = `
                    <h2>Current weather in ${data.city}</h2>
                    <p><strong>Temperature:</strong> ${data.temperature}°F</p>
                    <p><strong>Condition:</strong> ${data.condition}</p>
                    <p><strong>Humidity:</strong> ${data.humidity}%</p>
                    <p><strong>Wind Speed:</strong> ${data.wind_speed} mph</p>
                `;
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);  // Debugging: log any errors
            weatherResult.innerHTML = `<p>Error fetching data: ${error.message}</p>`;
        });
});