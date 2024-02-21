import re


numbers = input()
matches = re.finditer(
    r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))", numbers)
print(*[number.group(0) for number in matches], end=" ")
