from collections import deque


chocolates = deque([int(i) for i in input().split(", ")])
cups_of_milk = deque([int(i) for i in input().split(", ")])

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()

    if cup_of_milk <= 0 and chocolate <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)

print("Great! You made all the chocolate milkshakes needed!" if milkshakes >=
      5 else "Not enough milkshakes.")

print(
    f"Chocolate: {', '.join(str(el) for el in chocolates)}"
    if chocolates else "Chocolate: empty")

print(
    f"Milk: {', '.join(str(el) for el in cups_of_milk)}"
    if cups_of_milk else "Milk: empty")
