def discounted_price(price: float, percent: float) -> float:
    if not (0 <= percent <= 100):
        raise ValueError("Percent must be 0 to 100")

    return price * (1 - percent / 100)

