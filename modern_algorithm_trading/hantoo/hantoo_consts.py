from dotenv import load_dotenv
import os

load_dotenv()


HANTOO_APP_KEY = os.getenv("HANTOO_APP_KEY")
HANTOO_APP_SECRET = os.getenv("HANTOO_APP_SECRET")

HANTOO_CANO = os.getenv("HANTOO_CANO")
HANTOO_PRDT_CD = os.getenv("HANTOO_PRDT_CD")

HANTOO_URL_TOKEN = "https://openapi.koreainvestment.com:9443/oauth2/tokenP"
HANTOO_URL_BALANCE = "https://openapi.koreainvestment.com:9443/uapi/overseas-stock/v1/trading/inquire-balance"

REAL_PORT = '9443'
VIRTUAL_PORT = '29443'

REAL_TRADING = 'TTTS3012R'
VIRTUAL_TRADING = 'VTTS3012R'
