from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    _valid_computer_types = {"Laptop", "Desktop Computer"}

    def __init__(self) -> None:
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str,
                       processor: str, ram: int) -> str:
        if type_computer not in self._valid_computer_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        to_build = Laptop if type_computer == "Laptop" else DesktopComputer
        computer = to_build(manufacturer, model)
        self.warehouse.append(computer)

        return computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str,
                      wanted_ram: int) -> str:
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.ram >= wanted_ram \
                    and computer.processor == wanted_processor:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")
