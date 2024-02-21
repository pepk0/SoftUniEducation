def reverse_string(word: str) -> str:
    return word[::-1]


while True:
    word_to_reverse = input()
    if word_to_reverse == "end":
        break

    reverse_word = reverse_string(word_to_reverse)
    print(f"{word_to_reverse} = {reverse_word}")
