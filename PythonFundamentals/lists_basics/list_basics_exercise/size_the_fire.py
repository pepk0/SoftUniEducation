level_of_fire = [el.split(" = ") for el in input().split("#")]
amount_of_water = int(input())

total_fire = 0
effort = 0
cells = []
levels = {
    "High": (81, 125),
    "Medium": (51, 80),
    "Low": (1, 50),
}

for category, fire_value in level_of_fire:
    fire_value = int(fire_value)
    lower_range, upper_range = levels[category]
    if (lower_range <= fire_value <= upper_range and
        fire_value <= amount_of_water):
        amount_of_water -= fire_value
        cells.append(fire_value)
        total_fire += fire_value
        effort += fire_value * 0.25
    else:
        continue

print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}", f"Total Fire: {total_fire}", sep="\n")
