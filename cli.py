import argparse
import sys
import requests
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.client import get_client
from bot.logging_config import setup_logging
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

def parse_args():
    parser = argparse.ArgumentParser(description = "Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol",help="Trading symbol, e.g. BTCUSDT")
    parser.add_argument("--side", help="BUY or SELL")
    parser.add_argument("--order_type", help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")
    return parser.parse_args()

def prompt_non_empty(message: str) -> str:
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty.")

def prompt_choice(message: str, valid_choices: set[str]) -> str:
    while True:
        value = input(message).strip().upper()
        if value in valid_choices:
            return value
        print(f"Invalid Input. Choose one of: {', '.join(valid_choices)}")

def prompt_positive_float(message: str) -> float:
    while True:
        value = input(message).strip()
        try:
            number = float(value)
            if number > 0:
                return number
            print("Value must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def confirm_order() -> bool:
    while True:
        value = input("Confirm order? (Y/N): ").strip().upper()
        if value in {"Y", "N"}:
            return value == "Y"
        print("Please enter Y or N.")

def collect_missing_inputs(args):
    if not args.symbol:
        args.symbol = prompt_non_empty("Enter symbol (e.g. BTCUSDT): ")
    
    if not args.side:
        args.side = prompt_choice("Enter side (BUY/SELL): ", {"BUY", "SELL"})
    
    if not args.order_type:
        args.order_type = prompt_choice("Enter order type (MARKET/LIMIT): ", {"MARKET", "LIMIT"})
    
    if args.quantity is None:
        args.quantity = prompt_positive_float("Enter quantity: ")
    
    if args.order_type and args.order_type.upper() == "LIMIT" and args.price is None:
        args.price = prompt_positive_float("Enter price: ")
    
    return args

def main():
    logger = setup_logging()

    try:
        args = parse_args()
        args = collect_missing_inputs(args)

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)

        price = None
        if order_type == "LIMIT":
            if args.price is None:
                raise ValueError("Price is required for LIMIT orders")
            price = validate_price(args.price)

        print("Order Request Summary")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity:.3f}")
        if price is not None:
            print(f"Price       : {price:.2f}")
        
        if not confirm_order():
            print("Order cancelled by user.")
            logger.info("Order cancelled before submission by user.")
            sys.exit(0)
        
        client = get_client()

        logger.info(
            "Order Request | symbol = %s side = %s type = %s quantity = %s price = %s",
            symbol, side, order_type, quantity, args.price
        )

        if order_type == "MARKET":
            if args.price is not None:
                logger.warning("Price was provided for MARKET order and will be ignored.")
            response = place_market_order(client, symbol, side, quantity)
        else:
            response = place_limit_order(client, symbol, side,quantity, price)
        
        logger.info("Order response: %s", response)
        
        print("\nOrder Response")
        print(f"orderId     : {response.get('orderId')}")
        print(f"status      : {response.get('status')}")
        print(f"executedQty : {response.get('executedQty')}")
        print(f"avgPrice    : {response.get('avgPrice')}")

        print("\nOrder placed successfully.")

    except BinanceAPIException as e:
        logger.exception("Binance API error : %s", e)
        print(f"API Error : {e.message}")
        sys.exit(1)
    except BinanceRequestException as e:
        logger.exception("Binance request error: %s",e)
        print(f"Request error: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        logger.exception("Network error: %s", e)
        print("Network error: Please check your internet connection.")
        sys.exit(1)
    except Exception as e:
        logger.exception("Execution failed: %s", e)
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()