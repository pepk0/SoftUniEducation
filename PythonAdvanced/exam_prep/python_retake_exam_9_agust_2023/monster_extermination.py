from collections import deque

killed_monsters = 0
monsters = deque([int(el) for el in input().split(",")])
soldiers_strikes = deque([int(el) for el in input().split(",")])

while monsters and soldiers_strikes:
    monster = monsters.popleft()
    strike = soldiers_strikes.pop()

    if strike >= monster:
        killed_monsters += 1
        if strike - monster > 0:
            if not soldiers_strikes:
                soldiers_strikes.append(strike - monster)
            else:
                soldiers_strikes[-1] += strike - monster
    else:
        left_over_monster = monster - strike
        monsters.append(left_over_monster)

if not monsters:
    print("All monsters have been killed!")

if not soldiers_strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
