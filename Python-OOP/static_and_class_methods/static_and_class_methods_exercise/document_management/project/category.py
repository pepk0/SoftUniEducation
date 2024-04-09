class Category:
    def __init__(self, _id: int, name: str) -> None:
        self.id = _id
        self.name = name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}"

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.id == other

        return id(self) == id(other)
