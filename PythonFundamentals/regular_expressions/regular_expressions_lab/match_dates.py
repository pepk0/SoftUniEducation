import re

date_text = input()
matches = re.finditer(
    r"\b(\d{2})([./-])([A-Z]{1}[a-z]{2})\2(\d{4})", date_text)

for date in matches:
    date, month, year = date.group(1, 3, 4)
    print(f"Day: {date}, Month: {month}, Year: {year}")
