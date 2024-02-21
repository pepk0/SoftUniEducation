import re


def decrypt_message(key: list, message: str) -> str:
    decrypted_message = ""
    key_index = 0
    message_index = 0
    while message_index < len(message):
        decrypted_message += chr(ord(message[message_index]) - key[key_index])
        message_index += 1
        key_index += 1
        if key_index >= len(key):
            key_index = 0
    return decrypted_message


def extract_information(key: list, message: str) -> str:
    hidden_information = decrypt_message(key, message)
    treasure_type = re.search(r"[&][A-Za-z]+[&]", hidden_information)
    treasure_coordinates = re.search(r"[<].+[>]", hidden_information)
    treasure = treasure_type.group(0).replace("&", "", 2)
    coordinates = treasure_coordinates.group(
        0).replace("<", "").replace(">", "")
    return f"Found {treasure} at {coordinates}"


cipher_key = [int(i) for i in input().split()]
while True:
    cryptic_message = input()
    if cryptic_message == "find":
        break
    print(extract_information(cipher_key, cryptic_message))
