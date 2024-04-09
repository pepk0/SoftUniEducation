from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    expense_per_race = 200_000

    def __init__(self, budget: int) -> None:
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        first_sponsorship, second_sponsorship = 0, 0

        if race_pos == 1:
            first_sponsorship = 1_000_000
        elif race_pos <= 3:
            first_sponsorship = 500_000
        if race_pos <= 5:
            second_sponsorship = 100_000
        elif race_pos <= 7:
            second_sponsorship = 50_000

        total_sponsorship = first_sponsorship + second_sponsorship
        revenue = total_sponsorship - self.expense_per_race
        self.budget += revenue

        return (f"The revenue after the race is {revenue}$. "
                f"Current budget {self.budget}$")
