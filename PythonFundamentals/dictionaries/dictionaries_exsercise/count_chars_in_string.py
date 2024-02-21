def count_chars(list_arg: str) -> dict:
    return_dict = {}
    for character in list_arg:
        if character not in return_dict:
            return_dict[character] = 0
        return_dict[character] += 1
    return return_dict


input_text = input().replace(" ", "")
print(*[f"{k} -> {v}" for k, v in count_chars(input_text).items()], sep="\n")
