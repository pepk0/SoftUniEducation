import re


def decipher_command(text: str) -> str:
    deciphered_message = ""
    match_pattern = r"[star]"
    key = len(re.findall(match_pattern, text, re.IGNORECASE))
    for letter in text:
        deciphered_message += chr(ord(letter) - key)
    return deciphered_message


def validate_command(text: str):
    deciphered_command = decipher_command(text)
    match_pattern = (r"@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)"
                     r"[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*")
    planet_name = re.search(match_pattern, deciphered_command)
    if planet_name:
        return planet_name.group(3), planet_name.group(1)


number_messages = int(input())
attacked_planets, destroyed_planets = [], []
for _ in range(number_messages):
    command = input()
    target = validate_command(command)
    if target:
        type_command, target_name = target
        if type_command == "A":
            attacked_planets.append(target_name)
        else:
            destroyed_planets.append(target_name)

print(f"Attacked planets: {len(attacked_planets)}")
for attacked_planet in sorted(attacked_planets):
    print(f"-> {attacked_planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for destroyed_planet in sorted(destroyed_planets):
    print(f"-> {destroyed_planet}")
