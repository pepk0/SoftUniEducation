number_days = int(input())
number_hours = int(input())
total_parking_tax = 0

for day in range(1, number_days + 1):
    daily_parking_tax = 0
    for hour in range(1, number_hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            parking_tax = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            parking_tax = 1.2
        else:
            parking_tax = 1

        daily_parking_tax += parking_tax
    total_parking_tax += daily_parking_tax
    
    print(f"Day: {day} - {daily_parking_tax:.2f} leva")
print(f"Total: {total_parking_tax:.2f} leva")
