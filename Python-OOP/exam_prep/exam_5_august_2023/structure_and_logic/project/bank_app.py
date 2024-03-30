from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    valid_loan_types = {"StudentLoan": StudentLoan,
                        "MortgageLoan": MortgageLoan}
    valid_client_types = {"Student": Student, "Adult": Adult}
    valid_loans_for_clients = {"Student": "StudentLoan",
                               "Adult": "MortgageLoan"}

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.loans: list = []
        self.clients: list = []
        self.granted_loans = 0
        self.granted_sum = 0

    def first_loan(self, loan_type: str) -> BaseLoan:
        first_loan = [loan for loan in self.loans if
                      loan.__class__.__name__ == loan_type]
        return first_loan[0] if first_loan else None

    def get_client_by_id(self, client_id: str) -> BaseClient:
        for client in self.clients:
            if client.client_id == client_id:
                return client

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.valid_loan_types:
            raise Exception("Invalid loan type!")

        new_loan = self.valid_loan_types[loan_type]()
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str,
                   income: float) -> str:
        if client_type not in self.valid_client_types:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.valid_client_types[client_type](client_name,
                                                          client_id, income)
        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> str:
        client = self.get_client_by_id(client_id)
        loan = self.first_loan(loan_type)

        if (self.valid_loans_for_clients[client.__class__.__name__] !=
                loan.__class__.__name__):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        self.granted_loans += 1
        self.granted_sum += loan.amount

        return (f"Successfully granted {loan_type} to {client.name} with ID "
                f"{client.client_id}.")

    def remove_client(self, client_id: str) -> str:
        client: BaseClient = self.get_client_by_id(client_id)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:
        total_increased_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                total_increased_loans += 1

        return f"Successfully changed {total_increased_loans} loans."

    def increase_clients_interest(self, min_rate: float) -> str:
        number_of_clients_affected = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                number_of_clients_affected += 1

        return f"Number of clients affected: {number_of_clients_affected}."

    def get_statistics(self) -> str:
        total_income = sum(x.income for x in self.clients)
        total_loan_sum = sum(x.amount for x in self.loans)

        if not self.clients:
            avg_client_interest = 0
        else:
            avg_client_interest = sum(x.interest for x in self.clients) / len(
                self.clients)

        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {total_income:.2f}\n"
                f"Granted Loans: {self.granted_loans}, Total Sum: "
                f"{self.granted_sum:.2f}\n"
                f"Available Loans: {len(self.loans)}, Total Sum: "
                f"{total_loan_sum:.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest:.2f}")
