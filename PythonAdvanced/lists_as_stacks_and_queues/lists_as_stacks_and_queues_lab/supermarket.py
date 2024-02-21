from collections import deque


line = deque()

while True:
    command = input()

    if command == "Paid":
        while line:
            print(line.popleft())
    elif command == "End":
        break
    else:
        line.append(command)

print(f"{len(line)} people remaining.")
