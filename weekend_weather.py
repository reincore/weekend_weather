import os
import requests
import json

def check_weather():
    API_KEY = os.getenv('VISUAL_CROSSING_WEATHER_API_KEY')
    IFTTT_KEY = os.getenv('IFTTT_API_KEY')

    url = "https://visual-crossing-weather.p.rapidapi.com/forecast"
    querystring = {
        "aggregateHours":"24",
        "forecastDays":"2",
        "location":"41.0264,28.9808",
        "contentType":"json",
        "unitGroup":"metric",
        "includeAstronomy":"false",
        "shortColumnNames":"true"
    }
    headers = {
        "X-Rapidapi-Key": API_KEY,
        "X-Rapidapi-Host": "visual-crossing-weather.p.rapidapi.com",
        "Host": "visual-crossing-weather.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    conditions = [value['conditions'] for value in data['locations']['41.0264,28.9808']['values']]

    for condition in conditions:
        condition_json = json.dumps({"value1": condition})
        requests.post(f"https://maker.ifttt.com/trigger/weather_check/with/key/{IFTTT_KEY}", data=condition_json)

if __name__ == "__main__":
    check_weather()
