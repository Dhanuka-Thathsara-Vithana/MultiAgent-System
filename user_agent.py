from weather_agent import WeatherAgent

class UserAgent:
    def __init__(self, unique_id, weather_agent):
        self.unique_id = unique_id
        self.weather_agent = weather_agent

    def request_weather_info(self):
        city = input("Enter city name: ")
        result = self.weather_agent.fetch_weather(city)
        if "error" in result:
            print("Error fetching weather data:", result["error"])
        else:
            print(f"Weather in {city}: {result['temperature']}°C, {result['condition']}.")

    def get_weather_alert(self):
        departure = input("Enter departure city: ")
        destination = input("Enter destination city: ")
        result = self.weather_agent.alert_weather_conditions(departure, destination)
        if result["status"] == "success":
            print(result["alert"])
        else:
            print("Error fetching weather data.")
