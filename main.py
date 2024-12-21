from weather_agent import WeatherAgent
from user_agent import UserAgent

if __name__ == "__main__":
    # Replace with your actual OpenWeatherMap API key
    API_KEY = "f46a611b8f63b0b9f31d885562c0f570"

    # Instantiate agents
    weather_agent = WeatherAgent(unique_id=1, api_key=API_KEY)
    user_agent = UserAgent(unique_id=2, weather_agent=weather_agent)

    # Command-line interface
    print("User Agent Program")
    print("1. Fetch weather for a city")
    print("2. Get weather alert for departure and destination cities")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        user_agent.request_weather_info()
    elif choice == "2":
        user_agent.get_weather_alert()
    else:
        print("Invalid choice. Exiting program.")
