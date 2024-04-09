from calendar import month_name


class DVD:
    def __init__(self, name: str, _id: int, creation_year: int,
                 creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int):
        _, mouth, year = [int(el) for el in date.split(".")]
        mouth = month_name[mouth]
        return cls(name, _id, year, mouth, age_restriction)

    def __repr__(self) -> str:
        rented = "rented" if self.is_rented else "not rented"
        return (f"{self.id}: {self.name} ({self.creation_month} "
                f"{self.creation_year}) has age restriction "
                f"{self.age_restriction}. Status: {rented}")

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other

        return id(self) == id(other)
