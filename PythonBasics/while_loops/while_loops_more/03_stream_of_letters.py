result = ""
secret_sequence = ""
phrase = ""

while True:

    input_letter = input()

    if input_letter == "End":
        break

    if not input_letter.isalpha():
        continue

    # we check if the the input letter is c, o, or n if it is and the
    # letter is not yet collected, we add it to the secret_sequence
    if ((input_letter == "c" or input_letter == "o" or input_letter == "n")
        and input_letter not in secret_sequence):
        secret_sequence += input_letter
        # if we have collected all 3 letters, we add the collected phrase
        # to the result and we reset the values of our holding variables
        # and continue collecting
        if len(secret_sequence) == 3:
            result += phrase + " "
            phrase, secret_sequence = "", ""
        continue

    phrase += input_letter

print(result)
