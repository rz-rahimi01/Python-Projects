import requests

API_KEY = "your_api_key_here"  # Get one for free at https://openweathermap.org/
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print("❌ City not found.")
            return

        print(f"\n🌍 Weather in {data['name']}, {data['sys']['country']}:")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        print(f"☁ Condition: {data['weather'][0]['description'].title()}")
    except requests.exceptions.RequestException:
        print("⚠ Network error. Please check your connection.")

def main():
    print("🌦 Welcome to the Weather App!")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("👋 Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
