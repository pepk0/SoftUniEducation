from collections import deque

worms = deque(int(i) for i in input().split())
holes = deque(int(i) for i in input().split())

matches = 0
total_worms = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
    else:
        if worm - 3 > 0:
            worms.append(worm - 3)

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and total_worms == matches:
    print("Every worm found a suitable hole!")
elif not worms and total_worms != matches:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join((str(el) for el in worms))}")

if holes:
    print(f"Holes left: {', '.join((str(el) for el in holes))}")
else:
    print("Holes left: none")
