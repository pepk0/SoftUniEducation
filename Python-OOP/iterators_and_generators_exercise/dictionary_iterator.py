class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.dictionary = dictionary
        self.keys_list = [key for key in dictionary]
        self.curr_state = -1

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        self.curr_state += 1
        if self.curr_state == len(self.keys_list):
            raise StopIteration
        key = self.keys_list[self.curr_state]
        return key, self.dictionary[key]
