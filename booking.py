from dataclasses import dataclass
@dataclass
class Booking:
    guest: str
    nights: int
    rate: float
    def total(self):
        return self.nights * self.rate
print(Booking('Aina', 2, 180).total())

