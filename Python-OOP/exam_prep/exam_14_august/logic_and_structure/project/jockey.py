class Jockey:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value.strip() == "":
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        if value < 18:
            raise ValueError(
                "Jockeys must be at least 18 to participate in the race!")
        self.__age = value
