import re


def capture_number(text: str):
    pattern = r"\d+"
    matches = re.findall(pattern, text)
    return matches


while True:
    input_text = input()
    if input_text:
        results = capture_number(input_text)
        if results:
            print(*results, end=" ")
    else:
        break
