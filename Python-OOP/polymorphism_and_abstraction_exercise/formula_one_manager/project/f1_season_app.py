from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    valid_team_names = {"Red Bull", "Mercedes"}

    def __init__(self) -> None:
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str,
                                 budget: int) -> str or None:
        if team_name not in self.valid_team_names:
            raise ValueError("Invalid team name!")

        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        else:
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int,
                         mercedes_pos: int) -> str:
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        ahead_of_race = "Mercedes" if mercedes_pos < red_bull_pos \
            else "Red Bull"

        red_bull_res = self.red_bull_team.calculate_revenue_after_race(
            red_bull_pos)
        mercedes_res = self.mercedes_team.calculate_revenue_after_race(
            mercedes_pos)

        return (f"Red Bull: {red_bull_res}. Mercedes: {mercedes_res}. "
                f"{ahead_of_race} is ahead at the {race_name} race.")
