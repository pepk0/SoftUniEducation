city = input()
quantity = float(input())
discount = 0

if city == "Sofia":
    if 0 <= quantity <= 500:
        discount = 0.05
    elif 500 < quantity <= 1000:
        discount = 0.07
    elif 1000 < quantity <= 10000:
        discount = 0.08
    elif quantity > 10000:
        discount = 0.12

elif city == "Varna":
    if 0 <= quantity <= 500:
        discount = 0.045
    elif 500 < quantity <= 1000:
        discount = 0.075
    elif 1000 < quantity <= 10000:
        discount = 0.1
    elif quantity > 10000:
        discount = 0.13

elif city == "Plovdiv":
    if 0 <= quantity <= 500:
        discount = 0.055
    elif 500 < quantity <= 1000:
        discount = 0.08
    elif 1000 < quantity <= 10000:
        discount = 0.12
    elif quantity > 10000:
        discount = 0.145

if discount <= 0:
    print("error")
else:
    total = quantity * discount
    print(f"{total:.2f}")