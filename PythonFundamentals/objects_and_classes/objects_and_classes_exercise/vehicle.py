class Vehicle:
    def __init__(self, type: str, model: str, price: int,
                 owner=None) -> None:
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner_: str) -> str:
        message = "Car already sold"
        if not self.owner:
            if self.price <= money:
                change = money - self.price
                message = (f"Successfully bought a {self.type}. "
                           f"Change: {change:.2f}")
                self.owner = owner_
            else:
                message = "Sorry, not enough money"
        return message

    def sell(self) -> str | None:
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self) -> str:
        to_return = f"{self.model} {self.type} is on sale: {self.price}"
        if self.owner:
            to_return = f"{self.model} {self.type} is owned by: {self.owner}"
        return to_return


# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)
