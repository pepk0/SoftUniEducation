import re


def find_name(text: str) -> str:
    pattern = r"[A-Za-z]"
    return "".join(re.findall(pattern, text))


def find_distance(text: str) -> int:
    pattern = r"[0-9]"
    matches = re.findall(pattern, text)
    return sum([int(i) for i in matches])


participants = {name: 0 for name in input().split(", ")}
while True:
    name_distance = input()
    if name_distance == "end of race":
        break
    name = find_name(name_distance)
    distance = find_distance(name_distance)
    if name in participants:
        participants[name] += distance

top_three = sorted(participants.items(), key=lambda x: -x[1])
print(f"1st place: {top_three[0][0]}", f"2nd place: {top_three[1][0]}",
      f"3rd place: {top_three[2][0]}", sep="\n")
