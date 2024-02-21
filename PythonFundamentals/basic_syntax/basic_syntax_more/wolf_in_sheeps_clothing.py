heard = [animal for animal in input().split(", ")][::-1]

for position, animal in enumerate(heard):
    
    if animal == "wolf" and position == 0:
        print("Please go away and stop eating my sheep")
        break

    elif animal == "wolf":
        print(f"Oi! Sheep number {position}! "
              "You are about to be eaten by a wolf!")

