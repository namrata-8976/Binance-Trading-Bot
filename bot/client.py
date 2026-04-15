from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

def get_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY", "").strip()
    api_secret = os.getenv("BINANCE_API_SECRET", "").strip()

    if not api_key or not api_secret:
        raise ValueError("Missing Binance API Key or Binance API Secret in .env")
    
    return Client(api_key, api_secret, testnet = True)


