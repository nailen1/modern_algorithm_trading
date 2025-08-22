from .basis import fetch_coingecko_response, map_response_to_data
from .consts import COINGECKO_APIBASE_URL

def get_coingecko_list_url() -> str:
    return f"{COINGECKO_APIBASE_URL}/list"

def get_coin_list() -> dict:
    response = fetch_coingecko_response(get_coingecko_list_url())
    return map_response_to_data(response)
