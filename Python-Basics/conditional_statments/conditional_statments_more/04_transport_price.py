km_to_travel = int(input())
time_of_travel = input()

price = 0
taxi_starting_price = 0

if km_to_travel < 20:
    taxi_starting_price = 0.7
    if time_of_travel == "day":
        price = 0.79
    elif time_of_travel == "night":
        price = 0.9

elif km_to_travel < 100:
    price = 0.09

elif km_to_travel >= 100:
    price = 0.06

price_of_travel = km_to_travel * price + taxi_starting_price

print(f"{price_of_travel:.2f}")