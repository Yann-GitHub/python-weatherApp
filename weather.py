from dotenv import load_dotenv
from pprint import pprint  # pretty print
import requests  # to make HTTP requests
import os  # to access environment variables

load_dotenv()


# Function to get the current weather data from the API OpenWeatherMap
def get_current_weather(city="Locquirec"):

    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n ** Current Weather Conditions ** \n")

    city = input("Enter the city name: ")

    # check for empty strings and string with only spaces
    if not bool(city.strip()):
        city = "Locquirec"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
