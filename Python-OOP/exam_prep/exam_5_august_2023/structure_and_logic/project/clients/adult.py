from project.clients.base_client import BaseClient


class Adult(BaseClient):
    initial_interest_percent = 4.0

    def __init__(self, name: str, client_id: str, income: float) -> None:
        super().__init__(name, client_id, income, self.initial_interest_percent)

    def increase_clients_interest(self) -> None:
        self.interest += 2.0
