def replace_character(str_word: str) -> str:
    result = ""
    for character in str_word:
        result += chr(ord(character) + 3)
    return result


message = input()
print(replace_character(message))
