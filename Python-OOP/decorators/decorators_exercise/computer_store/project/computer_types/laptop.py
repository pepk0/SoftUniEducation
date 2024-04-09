from math import log2

from project.computer_types.computer import Computer


class Laptop(Computer):
    _available_processors = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }
    _max_ram: int = 64

    def __init__(self, manufacturer: str, model: str) -> None:
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int) -> str:
        if not log2(ram).is_integer() or ram > self._max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop "
                             f"{self.manufacturer} {self.model}!")

        if processor not in self._available_processors:
            raise ValueError(f"{processor} is not compatible with "
                             f"laptop {self.manufacturer} {self.model}!")

        self.ram, self.processor = ram, processor
        self.price = int(log2(ram)) * 100 + self._available_processors.get(
            processor)

        return (f"Created {self.manufacturer} {self.model} with "
                f"{self.processor} and {self.ram}GB RAM for {self.price}$.")
