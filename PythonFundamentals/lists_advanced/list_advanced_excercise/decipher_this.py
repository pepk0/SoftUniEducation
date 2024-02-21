def decipher(string: str) -> str:
    word_as_list = [s for s in string]
    num_index = 0
    number = ""
    while word_as_list[num_index].isdecimal():
        number += word_as_list[num_index]
        num_index += 1
    word_as_list = [chr(int(number))] + word_as_list[num_index::]
    word_as_list[1], word_as_list[-1] = word_as_list[-1], word_as_list[1]
    return "".join(word_as_list)


deciphered_words = [decipher(word) for word in input().split()]
print(*deciphered_words)
