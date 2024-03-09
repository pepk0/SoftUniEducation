class Customer:
    def __init__(self, name: str, age: int, _id: int) -> None:
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds: list = []

    def __repr__(self) -> str:
        return (f"{self.id}: {self.name} of age {self.age} has "
                f"{len(self.rented_dvds)} rented DVD's "
                f"({', '.join(dvd.name for dvd in self.rented_dvds)})")

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other

        return id(self) == id(other)
