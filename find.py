import requests

def current():
    requests.get("https://weather.com/weather/todays").content