morse_code_mapping = {'..-.': 'F', '-..-': 'X',
                      '.--.': 'P', '-': 'T',
                      '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                      '---': 'O', '-.-': 'K', '..': 'I',
                      '.-..': 'L', '-.--': 'Y',
                      '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                      '-...': 'B', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                      '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S'}

morse_code_text = input().split(" | ")
decrypted_message = ""
for word in morse_code_text:
    decrypted_message += " "
    for letter in word.split():
        decrypted_message += morse_code_mapping[letter]
print(decrypted_message.strip())
