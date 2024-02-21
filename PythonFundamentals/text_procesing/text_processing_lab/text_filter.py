def replace_banned_word(word: str) -> str:
    return "*" * len(word)


banned_words = set(input().split(", "))
text = input()

for word in banned_words:
    text = text.replace(word, replace_banned_word(word))

print(text)
