chicken_menu = 10.35
fish_menu = 12.4
vegetarian_menu = 8.15
delivery_price = 2.5

number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

food_price = (number_chicken_menu * chicken_menu) + (number_fish_menu \
           * fish_menu) + (number_vegetarian_menu * vegetarian_menu)

desert_price = food_price * 0.2 # desert is 20% of final food price

total_price = food_price + desert_price + delivery_price

print(round(total_price, 2))