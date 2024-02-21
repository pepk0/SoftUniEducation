from math import floor, ceil

number_days = int(input())
food_left_for_pets = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

food_dog_needs = dog_food_per_day * number_days
food_cat_needs = cat_food_per_day * number_days
food_turtle_needs = (turtle_food_per_day / 1000) * number_days

total_food_needed = food_dog_needs + food_cat_needs + food_turtle_needs

if food_left_for_pets >= total_food_needed:
    
    food_leftover = floor(food_left_for_pets - total_food_needed)
    print(f"{food_leftover} kilos of food left.")

else:

    more_food_needed = ceil(total_food_needed - food_left_for_pets)
    print(f"{more_food_needed} more kilos of food are needed.")