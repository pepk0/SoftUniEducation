def char_range(start: str, end: str) -> list:
    result = []
    start_range = ord(start) + 1
    end_range = ord(end)
    for i in range(start_range, end_range):
        result.append(chr(i))
    return result


first_character = input()
second_character = input()
print(*char_range(first_character, second_character), sep=" ")
