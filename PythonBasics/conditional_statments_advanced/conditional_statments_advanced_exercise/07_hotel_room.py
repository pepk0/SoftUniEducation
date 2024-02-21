month = input()
lodge = int(input())

apartment_price = 0
studio_price = 0

if month == "May" or month == "October":
    studio_price = 50
    if 7 < lodge <= 14:
        studio_price *= 1 - 0.05
    elif lodge > 14:
        studio_price *= 1- 0.3
    apartment_price = 65

elif month == "June" or month == "September":
    studio_price = 75.2
    if lodge > 14:
        studio_price *= 1 - 0.2
    apartment_price = 68.7

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if lodge > 14:
    apartment_price *= 1 - 0.1

total_studio_price = lodge * studio_price
total_apartment_price = lodge * apartment_price

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")