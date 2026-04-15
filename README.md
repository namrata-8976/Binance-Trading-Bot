# Binance Futures Testnet Trading Bot
A simple Python CLI application for placing MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).  

## Features

- Place MARKET and LIMIT orders
- Supports both BUY and SELL
- Works with Binance Futures Testnet
- Input validation for symbol, side, order type, quantity, and price
- Logs API requests, responses, and errors to a log file
- Handles invalid input, API errors, and request failures
- Supports:
  - CLI mode using command-line arguments
  - Interactive mode with user prompts and order confirmation
    
## Requirements
- Python 3.x
- Binance Futures Testnet account
- Binance Futures Testnet API key and secret

1. Setup
pip install -r requirements.txt

2. .env format
BINANCE_API_KEY = your_key
BINANCE_API_SECRET = your_secret

The steps to get your api key and secret is:
1. Go to https://testnet.binancefuture.com
2. In the drop down of Account symbol in top right corner click Demo Trading API and create API
3. Copy API key and Secret key

3.How to run?
i. CLI Mode
Example:
py cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
ii. Interactive Mode
Example:
py cli.py
Enter symbol (e.g. BTCUSDT): BTCUSDT
Enter side (BUY/SELL): SELL
Enter order type (MARKET/LIMIT): LIMIT
Enter quantity: 0.01
Enter price: 80000
Order Request Summary
Symbol      : BTCUSDT
Side        : SELL
Order Type  : LIMIT
Quantity    : 0.010
Price       : 80000.00
Confirm order? (Y/N): Y
