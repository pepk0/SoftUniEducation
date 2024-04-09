class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.curr_state: int = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_state += 1
        if self.curr_state == self.count:
            raise StopIteration
        return self.curr_state * self.step

#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
