def smallest_number(list_arg: list) -> int:
    smallest_num = 0
    for i in range(len(list_arg)):
        if list_arg[i] <= list_arg[smallest_num]:
            smallest_num = i
    return list_arg[smallest_num]


numbers = [int(input()) for _ in range(3)]
print(smallest_number(numbers))
