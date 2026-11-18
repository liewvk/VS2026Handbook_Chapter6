def calculate_total(price: float, quantity: int) -> float:
    subtotal = price * quantity
    discount = subtotal * 0.10 if subtotal >= 200 else 0.0
    return round(subtotal - discount, 2)
 
def print_invoice(price: float, quantity: int) -> None:
    print(f'Final amount: RM{calculate_total(price, quantity):.2f}')
 
if __name__ == '__main__':
    print_invoice(100.0, 3)

