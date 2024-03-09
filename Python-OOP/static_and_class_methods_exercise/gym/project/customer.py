from project.next_id import NextId


class Customer(NextId):

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.id = self.set_next_id()
        self.get_next_id()

    def __repr__(self) -> str:
        return (f"Customer <{self.id}> {self.name}; Address: {self.address}; "
                f"Email: {self.email}")
