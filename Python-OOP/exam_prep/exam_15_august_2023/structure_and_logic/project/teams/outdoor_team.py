from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    initial_budget = float(1000)

    def __init__(self, name: str, country: str, advantage: int) -> None:
        super().__init__(name, country, advantage, self.initial_budget)

    def win(self) -> None:
        self.wins += 1
        self.advantage += 115
