def eliminate_substring(string: str, substring: str) -> str:
    while substring in string:
        string = string.replace(substring, "", 1)
    return string


substring = input()
input_string = input()
print(eliminate_substring(input_string, substring))
