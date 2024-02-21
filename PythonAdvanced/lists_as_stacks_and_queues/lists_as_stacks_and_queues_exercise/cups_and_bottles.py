from collections import deque


cups = deque([int(i) for i in input().split()])
bottles = deque([int(i) for i in input().split()])

wasted_water = 0

while cups and bottles:
    bottle = bottles.pop()
    cup = cups.popleft()

    cup_leftover = cup - bottle
    bottle_leftover = bottle - cup

    if cup_leftover > 0:
        cups.appendleft(cup_leftover)

    if bottle_leftover > 0:
        wasted_water += bottle_leftover

if not cups:
    print(f"Bottles:", *bottles, sep=" ")
if not bottles:
    print(f"Cups:", *cups, sep=" ")
print(f"Wasted litters of water: {wasted_water}")
