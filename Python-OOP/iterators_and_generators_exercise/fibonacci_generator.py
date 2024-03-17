def fibonacci() -> int:
    first_num, second_num = 0, 1
    while True:
        curr = first_num
        first_num, second_num = second_num, first_num + second_num
        yield curr
