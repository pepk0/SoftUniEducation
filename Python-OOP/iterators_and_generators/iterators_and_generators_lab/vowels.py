class vowels:
    def __init__(self, string: str) -> None:
        self.string = string
        self.curr_state = -1
        self.string_vowels = [el for el in string if el.lower() in "ayouei"]

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.curr_state += 1
        if self.curr_state == len(self.string_vowels):
            raise StopIteration
        return self.string_vowels[self.curr_state]

#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
