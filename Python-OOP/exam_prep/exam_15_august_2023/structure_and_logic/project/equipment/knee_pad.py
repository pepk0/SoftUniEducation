from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    protection: int = 120
    price: float = 15.0

    def __init__(self) -> None:
        super().__init__(self.protection, self.price)

    def increase_price(self) -> None:
        self.price *= 1.2
