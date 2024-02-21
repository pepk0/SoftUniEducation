import re


def count_occurrences(text: str, word: str) -> int:
    matches = re.findall(f"\\b{word}\\b", text, re.IGNORECASE)
    return len(matches)


input_text = input()
target_word = input()
print(count_occurrences(input_text, target_word))
