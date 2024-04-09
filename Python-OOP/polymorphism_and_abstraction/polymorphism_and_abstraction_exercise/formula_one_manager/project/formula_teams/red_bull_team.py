from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    expense_per_race = 250_000

    def __init__(self, budget: int) -> None:
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        first_sponsorship, second_sponsorship = 0, 0

        if race_pos == 1:
            first_sponsorship = 1_500_000
        elif race_pos <= 2:
            first_sponsorship = 800_000
        if race_pos <= 8:
            second_sponsorship = 20_000
        elif race_pos <= 10:
            second_sponsorship = 10_000

        total_sponsorship = first_sponsorship + second_sponsorship
        revenue = total_sponsorship - self.expense_per_race
        self.budget += revenue

        return (f"The revenue after the race is {revenue}$. "
                f"Current budget {self.budget}$")
