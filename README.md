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

Install dependencies using:
```
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in the project root and add:
```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

## How to Get Binance Futures Testnet API Credentials

- Open the [Binance Futures Testnet website](https://testnet.binancefuture.com).
- Log in or create a testnet account.
- Click the account/profile icon in the top-right corner.
- Open Demo Trading API.
- Create a new API key.
- Copy and save the API Key and Secret Key.

## How to Run

1. CLI Mode

Example MARKET Order:
```
py cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```
Example LIMIT Order:

```
py cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 80000
```

2. Interactive Mode

Run
```
py cli.py
```

Example Flow:
```
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
```
## Assumptions

