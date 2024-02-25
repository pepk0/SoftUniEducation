class Song:
    def __init__(self, name: str, length: float, single: bool) -> None:
        self.name = name
        self.length = length
        self.single = single

    def get_info(self) -> str:
        return f"{self.name} - {self.length}"

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other

        return id(self) == id(other)
