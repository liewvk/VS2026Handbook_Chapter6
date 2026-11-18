from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int
    category: str

    def stock_value(self) -> float:
        return self.price * self.quantity

