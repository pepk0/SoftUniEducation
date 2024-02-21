bulging_floors = int(input())
floor_flats = int(input())

for floor in range(bulging_floors, 0, -1):
    for flat in range(floor_flats):
        
        flat_type = "O"        

        if floor == bulging_floors:
            flat_type = "L"
        
        elif floor % 2 != 0:
            flat_type = "A"

        print(f"{flat_type}{floor}{flat}", end=" ")

    print()   