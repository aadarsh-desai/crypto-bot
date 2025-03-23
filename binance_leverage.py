from binance.client import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

# Set leverage for futures
symbol = 'SOLUSDT'  # or 'SOLUSDT' as per your choice
leverage = 20
response = client.futures_change_leverage(symbol=symbol, leverage=leverage)
print(response)
