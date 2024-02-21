budget = float(input())
season = input()

car = ""
car_type = ""
price = 0

if budget <= 100:
    car_type = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    else:
        car = "Jeep"
        price = budget * 0.65

elif 100 < budget <= 500:
    car_type = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    else:
        car = "Jeep"
        price = budget * 0.80

elif budget > 500:
    car_type = "Luxury class"
    car = "Jeep"
    price = budget * 0.9

print(f"{car_type}\n{car} - {price:.2f}")
