def merge_string(start_idx: int, end_idx: int, list_arg: list) -> None:
    if start_idx < 0:
        start_idx = 0
    if end_idx >= len(list_arg):
        end_idx = len(list_arg) - 1
    merged_string = ""
    for i in range(start_idx, end_idx + 1):
        merged_string += list_arg[i]
    list_arg[start_idx:end_idx + 1] = [merged_string]


def divide_string(idx: int, parts: int, list_arg: list) -> list:
    word_as_list = [s for s in list_arg[idx]]
    elements = len(word_as_list) // parts
    new_word = []
    for _ in range(parts):
        result = ""
        for _ in range(elements):
            result += word_as_list.pop(0)
        new_word.append(result)
    if word_as_list:
        new_word[-1] += "".join(word_as_list)
    return new_word


data = [word for word in input().split()]
while True:
    command, *arguments = input().split()

    if command == "merge":
        start_index = int(arguments[0])
        end_index = int(arguments[1])
        merge_string(start_index, end_index, data)
    elif command == "divide":
        index = int(arguments[0])
        equal_parts = int(arguments[1])
        data = (data[:index] + divide_string(index, equal_parts, data) 
                + data[index + 1:])
    else:
        break

print(*data)
