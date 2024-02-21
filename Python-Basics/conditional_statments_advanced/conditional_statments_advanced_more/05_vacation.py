budget = float(input())
season = input()

destination = ""
accommodation = ""
price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        price = budget * 0.65
    else:
        price = budget * 0.45

elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        price = budget * 0.80
    else:
        price = budget * 0.6

elif budget > 3000:
    accommodation = "Hotel"
    price = budget * 0.9

if season == "Summer":
    destination = "Alaska"
else:
    destination = "Morocco"

print(f"{destination} - {accommodation} - {price:.2f}")
