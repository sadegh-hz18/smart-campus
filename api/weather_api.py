import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=35.7&longitude=51.4"
    "&current_weather=true"
)

response = requests.get(url)
data = response.json()

print("Current temperature:", data["current_weather"]["temperature"])