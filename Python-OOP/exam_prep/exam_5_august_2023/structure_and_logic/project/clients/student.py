from project.clients.base_client import BaseClient


class Student(BaseClient):
    initial_interest_percent = 2.0

    def __init__(self, name: str, client_id: str, income: float) -> None:
        super().__init__(name, client_id, income, self.initial_interest_percent)

    def increase_clients_interest(self) -> None:
        self.interest += 1.0
