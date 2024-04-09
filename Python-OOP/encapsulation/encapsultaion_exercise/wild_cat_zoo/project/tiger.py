from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name: str, gender: str, age: int,
                 money_for_care: int = 45) -> None:
        super().__init__(name, gender, age, money_for_care)
