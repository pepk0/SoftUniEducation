def valid_substring(string: str, list_arg: list) -> bool:
    for word in list_arg:
        if string in word:
            return True
    return False


string_sequence_one = [el for el in input().split(", ")]
string_sequence_two = [el for el in input().split(", ")]
print([word for word in string_sequence_one if valid_substring(
    word, string_sequence_two)])
