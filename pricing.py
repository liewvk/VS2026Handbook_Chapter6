def final_price(price, discount=0.0):
    if price < 0 or not 0 <= discount <= 1:
        raise ValueError('Invalid price or discount')
    return round(price * (1 - discount), 2)
print(final_price(100, .15))

