from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    percent_interest_rate = 1.5
    loan_amount = float(2000)

    def __init__(self) -> None:
        super().__init__(self.percent_interest_rate, self.loan_amount)

    def increase_interest_rate(self) -> None:
        self.interest_rate += 0.2
