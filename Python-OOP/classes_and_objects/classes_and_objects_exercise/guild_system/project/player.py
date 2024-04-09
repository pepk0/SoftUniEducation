class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild: str = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return (f"Skill {skill_name} added to the collection "
                    f"of the player {self.name}")

        return "Skill already added"

    def player_info(self) -> str:
        skills = "\n".join(f"==={n} - {c}" for n, c in self.skills.items())
        return (f"Name: {self.name}\nGuild: {self.guild}\n"
                f"HP: {self.hp}\nMP: {self.mp}\n{skills}")

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.name == other

        return id(self) == id(other)
