import os
import requests
import logging

def weekend_weather():
    # Set up logging
    logging.basicConfig(filename='logs.txt', level=logging.INFO)

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

    # Ensure there are at least 3 conditions
    conditions += [""] * max(0, 3 - len(conditions))

    condition_data = {"value1": conditions[0], "value2": conditions[1], "value3": conditions[2]}
    response = requests.post(f"https://maker.ifttt.com/trigger/weekend_weather/with/key/{IFTTT_KEY}", data=condition_data)
    logging.info(f"Status code: {response.status_code}")
    logging.info(f"Response text: {response.text}")

if __name__ == "__main__":
    weekend_weather()
