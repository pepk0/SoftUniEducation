from collections import deque


dispenser_liters = int(input())
line = deque()

while True:
    command = input()
    if command == "Start":
        break
    line.append(command)

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif len(command) == 2:
        dispenser_liters += int(command[1])
    else:
        requested_liters = int(command[0])
        person = line.popleft()
        if requested_liters <= dispenser_liters:
            print(f"{person} got water")
            dispenser_liters -= requested_liters
        else:
            print(f"{person} must wait")

print(f"{dispenser_liters} liters left")
