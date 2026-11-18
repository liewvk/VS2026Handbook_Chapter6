from dataclasses import dataclass
 
@dataclass
class Product:
    name: str
    unit_price: float
    quantity: int
    def total(self) -> float:
        return self.unit_price * self.quantity
 
cart = [Product('Pen', 2.5, 10), Product('Notebook', 7.0, 3)]
for item in cart:
    print(f'{item.name}: RM{item.total():.2f}')

