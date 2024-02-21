import re


def extract_email(text: str) -> list:
    pattern = (r"(?<=\s)[A-Za-z0-9]+[\.\_\-]*"
               r"[A-Za-z0-9]+@[A-Za-z-]+\.?[A-Za-z]+\.{1}[A-Za-z]+")
    matches = re.findall(pattern, text)
    return matches


sentence = input()
print(*extract_email(sentence), sep="\n")
