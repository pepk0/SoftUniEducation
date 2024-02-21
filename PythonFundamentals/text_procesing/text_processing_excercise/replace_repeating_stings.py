string_input = input()
result = ""

for character in string_input:
    if not result or character != result[-1]:
        result += character

print(result)
