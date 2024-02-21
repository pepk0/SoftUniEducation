def remove_vowels(string: str) -> str:
    vowels = {'a', 'o', 'u', 'e', 'i'}
    return "".join([el for el in string_text if el.lower() not in vowels])


string_text = input()
print(remove_vowels(string_text))
