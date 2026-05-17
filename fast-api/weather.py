import httpx

def get_current_weather(city: str):
    """
    Fetch the current real-time temperature and weather condition for a given city.
    """
    print(f"Fetching weather data for {city}...")
    
    # Target URL for the free weather API. '?format=j1' requests JSON format.
    url = f"https://wttr.in/{city}?format=j1"
    
    # Send a GET request to the API using httpx
    response = httpx.get(url)
    
    # Raise an exception if the request fails (e.g., bad network or invalid city)
    response.raise_for_status() 
    
    # Parse the JSON response into a Python dictionary
    data = response.json()
    
    # Extract the current temperature (in Celsius) and weather description
    current_temp = int(data['current_condition'][0]['temp_C'])
    condition = data['current_condition'][0]['weatherDesc'][0]['value']
    
    return current_temp, condition

# --- Test Block ---
# The code below only runs when you execute this script directly
if __name__ == "__main__":
    # You can change "Berlin" to your target city (e.g., "London", "New York")
    my_city = "Berlin" 
    
    try:
        temp, weather_desc = get_current_weather(my_city)
        print("✅ Data received successfully!")
        print(f"🌍 City: {my_city}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"☁️ Condition: {weather_desc}")
    except Exception as e:
        print(f"❌ Failed to fetch weather data. Error: {e}")