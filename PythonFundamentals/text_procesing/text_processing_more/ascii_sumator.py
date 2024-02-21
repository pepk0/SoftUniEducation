def sum_ascii(start: str, stop: str, text: str) -> int:
    ascii_sum = 0
    valid_character_range = range(ord(start) + 1, ord(stop))
    for character in text:
        if ord(character) in valid_character_range:
            ascii_sum += ord(character)
    return ascii_sum


range_start = input()
range_stop = input()
characters = input()
print(sum_ascii(range_start, range_stop, characters))
