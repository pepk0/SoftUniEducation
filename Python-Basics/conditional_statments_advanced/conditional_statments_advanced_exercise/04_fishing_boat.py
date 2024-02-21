fishing_budget = int(input())
season = input()
number_fisherman = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000

elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if number_fisherman <= 6:
    boat_rent *= 1 - 0.1
elif 7 <= number_fisherman <= 11:
    boat_rent *= 1 - 0.15
elif number_fisherman >= 12:
    boat_rent *= 1 - 0.25

if number_fisherman % 2 == 0 and season != "Autumn":
    boat_rent *= 1 - 0.05

if fishing_budget >= boat_rent:
    money_left_over = fishing_budget - boat_rent
    print(f"Yes! You have {money_left_over:.2f} leva left.")

else:
    money_needed = boat_rent - fishing_budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
