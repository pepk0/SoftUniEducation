class sequence_repeat:
    def __init__(self, sequence: str, repeat: int) -> None:
        self.sequence = sequence
        self.repeat = repeat
        self.curr_state: int = -1

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.curr_state += 1
        sequence_index = self.curr_state % len(self.sequence)
        if self.curr_state == self.repeat:
            raise StopIteration
        return self.sequence[sequence_index]
