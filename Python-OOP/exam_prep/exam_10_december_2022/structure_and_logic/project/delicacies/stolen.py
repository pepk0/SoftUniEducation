from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    DELICACY_PORTION = 250

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, self.DELICACY_PORTION, price)

    def details(self) -> str:
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
