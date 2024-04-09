def genrange(start: int, end: int):
    for number in range(start, end + 1):
        yield number

#
# print(list(genrange(1, 10)))
