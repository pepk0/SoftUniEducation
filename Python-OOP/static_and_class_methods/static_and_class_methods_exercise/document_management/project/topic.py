class Topic:
    def __init__(self, _id: int, topic: str, storage_folder: str) -> None:
        self.id = _id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str) -> None:
        self.storage_folder = new_storage_folder
        self.topic = new_topic

    def __repr__(self) -> str:
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.id == other

        return id(self) == id(other)
