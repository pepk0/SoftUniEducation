def make_dict(words: list) -> dict:
    return {words[i]: int(words[i + 1]) for i in range(0, len(words), 2)}


print(make_dict(input().split()))
