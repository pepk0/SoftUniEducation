from project.computer_types.computer import Computer
from math import log2


class DesktopComputer(Computer):
    _available_processors = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800,
    }
    _max_ram: int = 128

    def __init__(self, manufacturer: str, model: str) -> None:
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int) -> str:
        if not log2(ram).is_integer() or ram > self._max_ram:
            raise ValueError(
                f"{ram}GB RAM is not compatible with desktop computer "
                f"{self.manufacturer} {self.model}!")

        if processor not in self._available_processors:
            raise ValueError(f"{processor} is not compatible with desktop "
                             f"computer {self.manufacturer} {self.model}!")

        self.ram, self.processor = ram, processor
        self.price = 100 * int(log2(ram)) + self._available_processors.get(
            processor)

        return (f"Created {self.manufacturer} {self.model} with "
                f"{self.processor} and {self.ram}GB RAM for {self.price}$.")
