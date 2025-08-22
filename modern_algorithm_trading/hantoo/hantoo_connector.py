import requests
import json
from .hantoo_consts import HANTOO_URL_TOKEN, HANTOO_APP_KEY, HANTOO_APP_SECRET, HANTOO_CANO, HANTOO_PRDT_CD, HANTOO_URL_BALANCE, DATA_TOKEN


def get_response_token():
    url_token = HANTOO_URL_TOKEN
    data_for_token = {
        "grant_type": "client_credentials",
        "appkey": HANTOO_APP_KEY,
        "appsecret": HANTOO_APP_SECRET
    }
    headers = {
        "content-type": "application/json"
    }
    response = requests.post(url_token, data=json.dumps(data_for_token), headers=headers)
    return response

def get_data_tokden():
    response = get_response_token()
    data = response.json()
    return data

def fetch_response_balance(tr_id, data_token=DATA_TOKEN):
    token_type = data_token['token_type']
    token = data_token['access_token']
    url = HANTOO_URL_BALANCE
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"{token_type} {token}",
        "appkey": HANTOO_APP_KEY,
        "appsecret": HANTOO_APP_SECRET,
        "tr_id": tr_id
    }
    params = {
        "CANO": HANTOO_CANO,
        "ACNT_PRDT_CD": HANTOO_PRDT_CD,
        "OVRS_EXCG_CD": "NASD",
        "TR_CRCY_CD": "USD",
        "CTX_AREA_FK200": "",
        "CTX_AREA_NK200": ""
    }
    response = requests.get(url, headers=headers, params=params)
    return response

def get_data_balance(tr_id, data_token=DATA_TOKEN):
    response = fetch_response_balance(tr_id, data_token)
    data = response.json()
    return data