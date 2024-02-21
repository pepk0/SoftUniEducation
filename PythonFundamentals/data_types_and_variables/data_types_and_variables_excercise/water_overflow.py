times_to_add_water = int(input())
tank_capacity = 255
total_water_added = 0

for _ in range(times_to_add_water):

    litters = int(input())

    if litters + total_water_added > tank_capacity:
        print("Insufficient capacity!")
        continue
    else:
        total_water_added += litters

print(total_water_added)
