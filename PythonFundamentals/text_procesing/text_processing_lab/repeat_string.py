def multiply_text(text: list) -> str:
    result = ""
    for word in text:
        result += word * len(word)
    return result


words_to_multiply = input().split()
print(multiply_text(words_to_multiply))
