from typing import List

from project.band_members.musician import Musician


class Band:
    def __init__(self, name: str) -> None:
        self.name = name
        self.members: List[Musician] = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value == "":
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

    def get_musician_types(self) -> set:
        return {x.__class__.__name__ for x in self.members}

    def __str__(self) -> str:
        return f"{self.name} with {len(self.members)} members."
