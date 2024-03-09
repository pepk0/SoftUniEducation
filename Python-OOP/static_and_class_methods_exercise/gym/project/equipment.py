from project.next_id import NextId


class Equipment(NextId):
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = self.set_next_id()
        self.get_next_id()

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
