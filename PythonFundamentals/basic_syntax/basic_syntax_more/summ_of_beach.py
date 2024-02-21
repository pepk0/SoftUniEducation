string = input().lower()
words_to_find = ("sand", "water", "fish", "sun")
count = 0

for word in words_to_find:
    occurrences = string.count(word)
    count += occurrences

print(count)
