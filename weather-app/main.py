from rich import print
from datetime import datetime
import requests  # Import requests library

def display_temperature(day, temperature, unit='C'):
    """Displays a temperature with day"""
    print(f"[blue]{day}[/blue]: {round(temperature)}º{unit}")

def display_current_weather(city):
    """Displays the current weather"""
    api_key = "b4697434f3a4b96oc63c0bff5tca4166"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch data for {city}. Please check the city name.")
        return

    current_weather_data = response.json()
    current_weather_temperature = current_weather_data["temperature"]["current"]

    display_temperature("Today", round(current_weather_temperature))

def display_forecast_weather(city_name):
    """Display the weather forecast of a city"""
    api_key = "b4697434f3a4b96oc63c0bff5tca4166"
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch forecast data for {city_name}.")
        return

    forecast_weather_data = response.json()
    print("\n[green bold underline]Forecast: [/green bold underline]")

    for day in forecast_weather_data['daily']:
        timestamp = day['time']
        date = datetime.fromtimestamp(timestamp)  # Ensure timestamp is in seconds
        formatted_day = date.strftime('%A')
        temperature = day['temperature']['day']

        if date.date() != datetime.today().date():
            display_temperature(formatted_day, temperature)

def credit():
    """Display a credit message"""
    print("\n[yellow]This app was built by Stella Bullo in Python[/yellow]")

def welcome():
    """Display a welcome"""
    print("[blue bold]Welcome to Stella's weather app [/blue bold]")

welcome()
city_name = input("Enter the city name: ").strip()

if city_name:
    display_current_weather(city_name)
    display_forecast_weather(city_name)
    credit()
else:
    print("Please enter a valid city name")
