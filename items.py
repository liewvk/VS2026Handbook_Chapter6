from dataclasses import dataclass
@dataclass
class Product:
 name: str
 price: float
 quantity: int

 def stock_value(self) -> float:
        return self.price * self.quantity

item = Product("Notebook", 8.50, 12)
print(item.name, item.stock_value())

