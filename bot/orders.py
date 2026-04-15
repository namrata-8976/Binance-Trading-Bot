def place_market_order(client, symbol: str, side: str, quantity: float):
    return client.futures_create_order(
        symbol = symbol,
        side = side,
        type = "MARKET",
        quantity = quantity,
    )

def place_limit_order(client, symbol: str, side: str, quantity: float, price: float):
    return client.futures_create_order(
        symbol = symbol,
        side = side,
        type = "LIMIT",
        timeInForce = "GTC",
        quantity = quantity,
        price = price,
    )