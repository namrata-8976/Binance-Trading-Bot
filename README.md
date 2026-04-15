# Binance Futures Testnet Trading Bot

A simple Python-based CLI application that can place orders on Binance Futures Testnet (USDT-M) and provide a clean, reusable structure with proper logging and error handling.

---

## About The Project

This project is a lightweight trading bot designed to interact with the Binance Futures Testnet using Python. It allows users to place orders programmatically while ensuring input validation, structured logging, and clean code organization.

---

## Getting Started

Follow these steps to run the project locally.

---

### Prerequisites

- Python 3.10 or higher
- Binance Futures Testnet account

---

### Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/namrata-8976/Binance-Trading-Bot.git
cd Binance-Trading-Bot
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory
```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```
> How to Get Binance Futures Testnet API Credentials
> - Open the [Binance Futures Testnet website](https://testnet.binancefuture.com).
> - Log in or register for a free testnet account
> - Navigate to Demo Trading API from the profile menu
> - Generate a new API key
> - Save both the API Key and Secret Key

### Usage

1. CLI Mode

Pass all inputs directly as arguments in a single command:

MARKET Order:
```bash
py cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```
LIMIT Order:

```bash
py cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 80000
```

2. Interactive Mode

Run the program without any arguments. The application will prompt for each required input:

```bash
py cli.py
```

Example session:
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
### Assumptions

- A valid .env file with testnet API credentials exists in the project root prior to execution.
- Quantity and price inputs are not validated against exchange-specific precision constraints.
- All LIMIT orders are submitted with GTC (Good Till Cancelled) as the time-in-force.

