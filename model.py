from datetime import date

class Medicine:
    def __init__(self, id: int, name: str, price: float, mfd: date, exp: date, quantity: int, power: int):
        self.id = id
        self.name = name
        self.price = price
        self.mfd = mfd
        self.exp = exp
        self.quantity = quantity
        self.power = power
