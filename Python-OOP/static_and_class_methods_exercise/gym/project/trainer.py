from project.next_id import NextId


class Trainer(NextId):
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = self.set_next_id()

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"
