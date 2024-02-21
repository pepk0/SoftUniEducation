import re

names = input()
matches = re.findall(r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b", names)
print(*[name for name in matches], sep=" ")
