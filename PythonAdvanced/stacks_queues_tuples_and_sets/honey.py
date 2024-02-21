from collections import deque


bees = deque([int(i) for i in input().split()])
nectars = [int(i) for i in input().split()]
honey_making_operators = deque(input().split())

operators = {
    "+": lambda x, y: abs(x + y), # redundant abs() calls here
    "-": lambda x, y: abs(x - y),
    "*": lambda x, y: abs(x * y), 
    "/": lambda x, y: abs(x / y),
}

honey_made = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar >= bee:
        if nectar == 0 and honey_making_operators[0] == "/":
            continue
        operator = operators[honey_making_operators.popleft()]
        honey_made += operator(bee, nectar) # could of added abs() here
    else:
        bees.appendleft(bee)
        continue

print(f"Total honey made: {honey_made}")

if bees:
    print(f"Bees left: {', '.join(str(el) for el in bees)}")

if nectars:
    print(f"Bees left: {', '.join(str(el) for el in nectars)}")
