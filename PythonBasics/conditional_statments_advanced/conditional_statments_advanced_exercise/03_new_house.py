rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

type_flower = input()
quantity_flowers = int(input())
budget = int(input())

flower_price = 0
price_modifier = 0

if type_flower == "Roses":
    flower_price = rose_price
    if quantity_flowers > 80:
        price_modifier = 0.1

elif type_flower == "Dahlias":
    flower_price = dahlia_price
    if quantity_flowers > 90:
        price_modifier = 0.15

elif type_flower == "Tulips":
    flower_price = tulip_price
    if quantity_flowers > 80:
        price_modifier = 0.15

elif type_flower == "Narcissus":
    flower_price = narcissus_price
    if quantity_flowers < 120:
        price_modifier = 2.15

elif type_flower == "Gladiolus":
    flower_price = gladiolus_price
    if quantity_flowers < 80:
        price_modifier = 2.2

total_flower_cost = quantity_flowers * flower_price * abs(1 - price_modifier)

if total_flower_cost <= budget:
    left_over_money = budget - total_flower_cost
    print(f"Hey, you have a great garden with {quantity_flowers} "
          f"{type_flower} and {left_over_money:.2f} leva left.")

else:
    money_needed = total_flower_cost - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
