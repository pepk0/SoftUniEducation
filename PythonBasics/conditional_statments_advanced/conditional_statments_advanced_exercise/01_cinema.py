premier_ticket_price = 12
normal_ticket_price = 7.5
discount_ticket_price = 5
total_income = 0

type_ticket = input()
cinema_room_rows = int(input())
cinema_room_columns = int(input())

if type_ticket == "Premiere":
    ticket_price = premier_ticket_price

elif type_ticket == "Normal":
    ticket_price = normal_ticket_price

elif type_ticket == "Discount":
    ticket_price = discount_ticket_price

total_seats = cinema_room_rows * cinema_room_columns
total_income = total_seats * ticket_price

print(f"{total_income:.2f} leva")
