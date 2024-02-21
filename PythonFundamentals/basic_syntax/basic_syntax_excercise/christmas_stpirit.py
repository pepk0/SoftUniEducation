quantity_decorations = int(input())
day_left_till_christmas = int(input())
total_price = 0
total_spirit = 0

for day in range(1, day_left_till_christmas + 1):

    if day % 11 == 0:
        quantity_decorations += 2

    if day % 2 == 0:
        total_price += (2 * quantity_decorations)
        total_spirit += 5

    if day % 3 == 0:
        total_price += (5 + 3) * quantity_decorations
        total_spirit += 3 + 10
        
    if day % 5 == 0:
        total_price += 15 * quantity_decorations
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
            
    if day % 10 == 0:
        total_spirit -= 20
        total_price += (5 + 3 + 15)

if day_left_till_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {int(total_price)}", 
      f"Total spirit: {int(total_spirit)}", sep="\n")
    

