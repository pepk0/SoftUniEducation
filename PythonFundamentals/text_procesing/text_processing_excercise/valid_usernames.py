def redundant_symbol(text_word: str) -> bool:
    return " " not in text_word


def length_check(text_word: str) -> bool:
    return 3 <= len(text_word) <= 16


def validate_symbols(text_word: str) -> bool:
    for character in text_word:
        if not character.isalnum():
            if character != "_" and character != "-":
                return False
    return True


def validate_username(string_text: str) -> bool:
    condition_one = redundant_symbol(string_text)
    condition_two = length_check(string_text)
    condition_tree = validate_symbols(string_text)
    return condition_one and condition_two and condition_tree


password_list = input().split(", ")
for word in password_list:
    if validate_username(word):
        print(word)
