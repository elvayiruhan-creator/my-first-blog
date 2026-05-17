import httpx

def get_weather_forecast(city: str):
    """
    Fetch a 3-day weather forecast for a given city.
    Returns a list of dictionaries containing date, average temperature, and condition.
    """
    print(f"Fetching 3-day forecast data for {city}...")
    url = f"https://wttr.in/{city}?format=j1"
    
    response = httpx.get(url)
    response.raise_for_status() 
    data = response.json()
    
    forecast_list = []
    
    # wttr.in 'weather' array always contains exactly 3 days of data
    for day_data in data['weather']:
        date_str = day_data['date']
        avg_temp = int(day_data['avgtempC'])
        
        # Extract midday weather condition (12:00 PM is index 4 in the hourly array)
        midday_condition = day_data['hourly'][4]['weatherDesc'][0]['value']
        
        forecast_list.append({
            "date": date_str,
            "temp": avg_temp,
            "condition": midday_condition
        })
        
    return forecast_list

# --- Test Block ---
if __name__ == "__main__":
    try:
        forecast = get_weather_forecast("Berlin")
        print("✅ 3-Day Forecast parsed successfully:")
        for day in forecast:
            print(f"- {day['date']}: {day['temp']}°C, {day['condition']}")
    except Exception as e:
        print(f"❌ Test failed: {e}")