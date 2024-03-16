class countdown_iterator:
    def __init__(self, number: int) -> None:
        self.number = number
        self.curr_state: int = number + 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.curr_state -= 1
        if self.curr_state == -1:
            raise StopIteration
        return self.curr_state
