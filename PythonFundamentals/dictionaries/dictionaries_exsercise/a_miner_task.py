resources = {}

while 1:
    item = input()
    if item == "stop":
        break
    quantity = int(input())
    if item not in resources:
        resources[item] = 0
    resources[item] += quantity

print(*[f"{k} -> {v}" for k, v in resources.items()], sep="\n")
