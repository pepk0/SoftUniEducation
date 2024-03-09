class NextId:
    id = 0

    @classmethod
    def set_next_id(cls) -> int:
        cls.id += 1
        return cls.id

    @classmethod
    def get_next_id(cls) -> int:
        return cls.id + 1

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.id == other

        return id(self) == id(other)
