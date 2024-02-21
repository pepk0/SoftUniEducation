from collections import deque
from math import floor


operations = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: floor(x / y),
}

expression = input().split()
line = deque()

for item in expression:
    if item not in operations:
        line.append(int(item))
    else:
        operation = operations[item]
        while len(line) > 1:
            first_n, second_n = line.popleft(), line.popleft()
            line.appendleft(operation(first_n, second_n))

print(line.popleft())
