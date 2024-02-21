room_for_one_person_price = 18
apartment_price = 25
presidential_apartment_price = 35

days_stayed = int(input())
accommodation = input()
rating = input()

nights_stayed = days_stayed - 1
price = 0
discount = 0

if accommodation == "room for one person":
    price = room_for_one_person_price

elif accommodation == "apartment":
    price = apartment_price
    if days_stayed < 10:
        discount = 0.3
    elif 10 <= days_stayed <= 15:
        discount = 0.35
    elif days_stayed > 15:
        discount = 0.5

elif accommodation == "president apartment":
    price = presidential_apartment_price
    if days_stayed < 10:
        discount = 0.1
    elif 10 <= days_stayed <= 15:
        discount = 0.15
    elif days_stayed > 15:
        discount = 0.2

total_price = nights_stayed * price * (1 - discount)

if rating == "positive":
    total_price *= 1 + 0.25
else:
    total_price *= 1 - 0.1

print(f"{total_price:.2f}")
