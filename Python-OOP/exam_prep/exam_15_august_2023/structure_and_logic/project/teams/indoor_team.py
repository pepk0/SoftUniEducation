from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    initial_budget = float(500)

    def __init__(self, name: str, country: str, advantage: int) -> None:
        super().__init__(name, country, advantage, self.initial_budget)

    def win(self) -> None:
        self.wins += 1
        self.advantage += 145
