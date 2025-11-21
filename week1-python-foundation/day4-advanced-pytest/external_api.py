import requests

def get_weather(city: str) -> dict:
    url = f"https://fake-weather-api.com/{city}"
    response = requests.get(url)
    return response.json()
