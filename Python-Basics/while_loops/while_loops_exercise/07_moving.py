room_width = int(input())
room_length = int(input())
room_height = int(input())
free_space = room_height * room_length * room_width

while free_space > 0:

    package = input()
    if package == "Done":
        break

    free_space -= int(package)

difference = abs(free_space)

if free_space <= 0:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")
