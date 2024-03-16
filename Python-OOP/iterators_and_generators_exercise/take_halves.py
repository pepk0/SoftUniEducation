def solution() -> tuple:
    def integers():
        curr_number = 0
        while True:
            curr_number += 1
            yield curr_number

    def halves():
        for integer in integers():
            yield integer / 2

    def take(numbers: int, sequence) -> list:
        return [next(sequence) for _ in range(numbers)]

    return take, halves, integers
