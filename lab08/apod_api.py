import requests

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "SxGsSvRUJzznvldEkX1AZ9gfZpe7khQCdN4kv1js"

def get_apod(date=None):
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch APOD. Status Code: {response.status_code}"}
