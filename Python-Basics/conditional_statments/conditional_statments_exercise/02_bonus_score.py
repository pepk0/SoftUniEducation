less_then_hundred_bonus = 5
greater_then_hundred_bonus = 0.2
greater_then_thousand_bonus = 0.1
even_number_bonus = 1
ends_with_five_bonus = 2

number = int(input())

bonus_points = 0

if number <= 100:
    bonus_points += less_then_hundred_bonus

elif number > 1000:
    bonus_points += number * greater_then_thousand_bonus

else:
    bonus_points += number * greater_then_hundred_bonus

if number % 2 == 0:
    bonus_points += even_number_bonus

elif number % 10 == 5:
    bonus_points += ends_with_five_bonus

total_points = bonus_points + number

print(bonus_points)
print(total_points)