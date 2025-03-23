from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("6c99a27e5727d38011a37f9ccec4a31a581a9bb7c3c7e8ecf054d7ba1da3abfa")
api_secret = os.getenv("7c2fde9aa087dc224f6488f31873ff32a67f786ca387bea81e2fc70cbde75f78")

client = Client(api_key, api_secret)

# Set leverage for futures
symbol = 'BTCUSDT'
leverage = 20
response = client.futures_change_leverage(symbol=symbol, leverage=leverage)
print(response)
