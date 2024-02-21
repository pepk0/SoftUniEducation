def concatenate_strings(string_len: int) -> str:
    result = ""

    for _ in range(string_len):
        result += input()

    return result


print(concatenate_strings(3))
