line = [int(i) for i in input().split()]
skips = int(input())

person = 0
skips -= 1
people_sequence = []

while line:
    next_person = person + skips
    while next_person >= len(line):
        next_person = next_person % len(line)
    people_sequence.append(str(line[next_person]))
    line.pop(next_person)
    person = next_person

print(f"[{','.join(people_sequence)}]")
