number_words = int(input())
synonym_dict = {}

for _ in range(number_words):
    word = input()
    synonym = input()
    if word not in synonym_dict:
        synonym_dict[word] = []
    synonym_dict[word].append(synonym)

for word, synonyms in synonym_dict.items():
    print(f"{word} -", end=" ")
    print(*synonyms, sep=", ")
