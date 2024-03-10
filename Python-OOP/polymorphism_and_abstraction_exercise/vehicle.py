from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        super().__init__(fuel_quantity, fuel_consumption)
        self.air_conditioner_consumption = 0.9

    def drive(self, distance: int) -> None:
        fuel_needed = distance * (
                self.fuel_consumption + self.air_conditioner_consumption)
        if fuel_needed < self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        super().__init__(fuel_quantity, fuel_consumption)
        self.air_conditioner_consumption = 1.6

    def drive(self, distance: int) -> None:
        fuel_needed = distance * (
                self.fuel_consumption + self.air_conditioner_consumption)
        if fuel_needed < self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * 0.95
