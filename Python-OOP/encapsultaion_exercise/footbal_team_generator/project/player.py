class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int,
                 shooting: int) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return (f"Player: {self.name}\nSprint: {self.__sprint}\nDribble: "
                f"{self.__dribble}\nPassing: {self.__passing}\n"
                f"Shooting: {self.__shooting}")

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.name == other

        return id(self) == id(other)
