cake_hight = int(input())
cake_width = int(input())
pieces_cake = cake_hight * cake_width


while pieces_cake > 0:

    pieces_to_take = input()
    if pieces_to_take == "STOP":
        break

    pieces_cake -= int(pieces_to_take)

difference = abs(pieces_cake)

if pieces_cake <= 0:
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{difference} pieces are left.")
