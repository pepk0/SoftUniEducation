class Stack:
    def __init__(self) -> None:
        self.data: list = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> None:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not self.data

    def __str__(self) -> str:
        return f"[{', '.join(f'{el}' for el in self.data[::-1])}]"
