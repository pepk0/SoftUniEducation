class custom_range:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.curr_state = self.start - 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.curr_state += 1
        if self.curr_state > self.end:
            raise StopIteration
        return self.curr_state

#
# for i in custom_range(1, 4):
#     print(i)
