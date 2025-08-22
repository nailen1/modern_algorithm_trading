import requests

def fetch_coingecko_response(url: str, params: dict | None = None) -> requests.Response:
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    return response

def map_response_to_data(response: requests.Response) -> dict:
    return response.json()
