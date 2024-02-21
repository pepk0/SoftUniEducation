season = input()
km_per_month = float(input())

percent_taxes = 0.1
total_km_driven = km_per_month * 4 # one season is 4 months
price_per_km = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.9
    else:
        price_per_km = 1.05

elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.1
    else:
        price_per_km = 1.25

elif 10000 < km_per_month <= 20000:
    price_per_km = 1.45

total_price_earned = total_km_driven * price_per_km * (1 - percent_taxes)

print(f"{total_price_earned:.2f}")
