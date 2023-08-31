import requests

def fetch_data_from_external_api():
    response = requests.get("https://restcountries.com/v3.1/all")
    data = response.json()
    return data
