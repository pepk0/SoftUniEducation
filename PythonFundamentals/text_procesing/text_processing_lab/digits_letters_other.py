text_to_process = input()

letters = ""
digits = ""
others = ""
for symbol in text_to_process:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else: # everything else is neither a digit or a symbol
        others += symbol

print(digits, letters, others, sep="\n")
