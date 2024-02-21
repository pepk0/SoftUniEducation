n_numbers = int(input())
stack = []

commands = {
    "1": lambda x: x.append(number),
    "2": lambda x: x.pop() if x else None,
    "3": lambda x: print(max(x)) if x else None,
    "4": lambda x: print(min(x)) if x else None
}

for _ in range(n_numbers):
    command = input().split()
    if len(command) > 1:
        number = int(command[1])
    commands[command[0]](stack)

stack.reverse()
print(*stack, sep=", ")
