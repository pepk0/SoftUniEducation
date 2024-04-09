class reverse_iter:
    def __init__(self, iterable) -> None:
        self.iterable = iterable[::-1]
        self.curr_state = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_state += 1
        if self.curr_state == len(self.iterable):
            raise StopIteration
        return self.iterable[self.curr_state]

# 
# reversed_list = reverse_iter("peter")
# for item in reversed_list:
#     print(item)
