import os
import requests

def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY is not set.")
        return

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        condition = data["current"]["condition"]["text"]
        temp = data["current"]["temp_c"]

        print(f"{city}/{data['location']['country']} {data['location']['localtime']} "
              f"Weather: {temp} Celsius, {condition}")

    except Exception as e:
        print(f"Failed to get weather: {e}")


if __name__ == "__main__":
    get_weather()
