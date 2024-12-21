import requests

class WeatherAgent:
    def __init__(self, unique_id, api_key):
        self.unique_id = unique_id
        self.api_key = api_key

    def fetch_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "condition": data["weather"][0]["description"]
                }
            elif response.status_code == 401:
                return {"error": "Unauthorized. Check your API key."}
            else:
                return {"error": f"HTTP {response.status_code}: {response.reason}"}
        except Exception as e:
            return {"error": str(e)}

    def alert_weather_conditions(self, departure_city, destination_city):
        departure_weather = self.fetch_weather(departure_city)
        destination_weather = self.fetch_weather(destination_city)

        if "error" in departure_weather or "error" in destination_weather:
            return {
                "status": "error",
                "departure_weather": departure_weather,
                "destination_weather": destination_weather
            }

        alert_message = f"Weather Alert:\n\n"
        alert_message += f"Departure City ({departure_city}):\n"
        alert_message += f"  - Temperature: {departure_weather['temperature']}°C\n"
        alert_message += f"  - Condition: {departure_weather['condition']}\n\n"
        alert_message += f"Destination City ({destination_city}):\n"
        alert_message += f"  - Temperature: {destination_weather['temperature']}°C\n"
        alert_message += f"  - Condition: {destination_weather['condition']}\n\n"

        issues = []
        for city, weather in [("Departure", departure_weather), ("Destination", destination_weather)]:
            if "rain" in weather["condition"].lower() or "storm" in weather["condition"].lower():
                issues.append(f"{city} City: {weather['condition'].capitalize()} may cause delays.")

        if issues:
            alert_message += "Potential Issues:\n" + "\n".join(issues)
        else:
            alert_message += "No significant weather-related issues expected."

        return {"status": "success", "alert": alert_message}
