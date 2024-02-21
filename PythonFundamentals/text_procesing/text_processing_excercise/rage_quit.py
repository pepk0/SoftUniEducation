text = input()
result = ""
temporary_string = ""
number = ""
index = 0

while index < len(text):
    if not text[index].isdigit():
        if text[index].isalpha():
            temporary_string += text[index].upper()
        else:
            temporary_string += text[index]
    else:
        for num_index in range(index, len(text)):
            if not text[num_index].isdigit():
                break
            number += text[num_index]
            index += 1
        result += temporary_string * int(number)
        number = ""
        temporary_string = ""
        continue
    index += 1

unique_symbols = len(set(result))
print(f"Unique symbols used: {unique_symbols}", result, sep="\n")
