from math import floor

group_size = int(input())
adventure_days = int(input())
coins = 0

for day in range(1, adventure_days + 1):

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins += (50 - group_size * 2)
    
    if day % 3 == 0:
        coins -= group_size * 3

    if day % 5 == 0:
        coins += group_size * 20
        if day % 3 == 0:
            coins -= group_size * 2

coins_per_person = floor(coins / group_size)
print(f"{group_size} companions received {coins_per_person} coins each.")
