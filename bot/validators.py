def validate_symbol(symbol: str) -> str:
    if not symbol or not symbol.strip():
        raise ValueError("Symbol is required")
    return symbol.strip().upper()

def validate_side(side: str) -> str:
    side = side.strip().upper()
    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.strip().upper()
    if order_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    return quantity

def validate_price(price: float) -> float:
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    return price
