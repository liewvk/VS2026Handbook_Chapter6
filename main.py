from models import Product
from discount import discounted_price

def main():
    product = Product("Notebook", 8.50, 12, "Stationery")
    print("Category:", product.category)
    print("Product:", product.name)
    print(f"Unit Price: RM{product.price:.2f}")
    print("Quantity:", product.quantity)

    total = product.stock_value()
    print(f"Stock Value: RM{total:.2f}")

    discount_percent = 15
    final_total = discounted_price(total, discount_percent)

    print(f"Discount: {discount_percent}%")
    print(f"Final Value: RM{final_total:.2f}")


if __name__ == "__main__":
    main()

