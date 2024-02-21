import re


phone_numbers = input()
matches = re.finditer(r"\+359+( |-)2\1\d{3}\1\d{4}\b", phone_numbers)
print(*[number.group(0) for number in matches], sep=", ")
