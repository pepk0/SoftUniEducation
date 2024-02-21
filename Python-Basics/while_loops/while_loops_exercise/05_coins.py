change = float(input()) 
change_in_cents = int(change * 100)
coins_used = 0

while change_in_cents > 0:
    
    if change_in_cents >= 200:
        change_in_cents -= 200
    
    elif change_in_cents >= 100:
        change_in_cents -= 100

    elif change_in_cents >= 50:
        change_in_cents -= 50

    elif change_in_cents >= 20:
        change_in_cents -= 20

    elif change_in_cents >= 10:
        change_in_cents -= 10

    elif change_in_cents >= 5:
        change_in_cents -= 5

    elif change_in_cents >= 2:
        change_in_cents -= 2

    elif change_in_cents >= 1:
        change_in_cents -= 1

    coins_used += 1    

print(coins_used)
