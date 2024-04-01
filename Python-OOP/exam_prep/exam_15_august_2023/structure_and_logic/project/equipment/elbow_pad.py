from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    protection: int = 90
    price: float = 25.0

    def __init__(self) -> None:
        super().__init__(self.protection, self.price)

    def increase_price(self):
        self.price *= 1.1
