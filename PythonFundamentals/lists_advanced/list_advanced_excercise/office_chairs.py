number_of_rooms = int(input())
leftover_chairs = 0
game_on = True

for room in range(1, number_of_rooms + 1):
    chairs, people = input().split()
    chairs = len(chairs)
    people = int(people)
    excess_chairs = chairs - people
    if excess_chairs < 0:
        print(f"{abs(excess_chairs)} more chairs needed in room {room}")
        game_on = False
    else:
        leftover_chairs += excess_chairs

if game_on:
    print(f"Game On, {leftover_chairs} free chairs left")

