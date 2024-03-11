class Account:
    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions: list = []
        self.balance = amount

    def handle_transaction(self, transaction_amount: int) -> str or None:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self.balance += transaction_amount
        self._transactions.append(transaction_amount)

        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int) -> str or None:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        self.handle_transaction(amount)

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.balance})"

    def __len__(self) -> int:
        return len(self._transactions)

    # THIS IS REDUNDANT IF WE HAVE A GETITEM OVERWRITTEN
    # def __iter__(self) -> int:
    #     for transaction in self._transactions:
    #         yield transaction

    def __reversed__(self) -> list:
        return self._transactions[::-1]

    def __lt__(self, other) -> bool:
        return self.balance < other.balance

    def __le__(self, other) -> bool:
        return self.balance <= other.balance

    def __eq__(self, other) -> bool:
        return self.balance == other.balance

    def __add__(self, other):
        new_account = Account(f"{self.owner}&{other.owner}",
                              self.amount + other.amount)

        new_account._transactions = self._transactions + other._transactions
        return new_account

    def __getitem__(self, index) -> int:
        return self._transactions[index]
