percent_from_budget_for_set = 0.1
number_of_extras_for_discount = 150
percent_costume_discount = 0.1

movie_budget = float(input())
number_extras = int(input())
price_per_costume = float(input())

set_price = movie_budget * percent_from_budget_for_set
costume_price = number_extras * price_per_costume

if number_extras > number_of_extras_for_discount:
    costume_price *= 1 - percent_costume_discount

movie_price = set_price + costume_price

if movie_budget < movie_price:
    money_needed = movie_price - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")

else:
    money_left = movie_budget - movie_price
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")