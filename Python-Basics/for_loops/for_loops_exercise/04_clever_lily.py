years_age = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())

gifted_money = 0
gifted_toys = 0
money_stolen = 0

for year in range(1, years_age + 1):

    if year % 2 == 0:
        gifted_money += year * 5 - 1
    else:
        gifted_toys += 1

money_from_toys = gifted_toys * single_toy_price
total_money_earned = money_from_toys + gifted_money

if total_money_earned >= washing_machine_price:
    money_left = total_money_earned - washing_machine_price
    print(f"Yes! {money_left:.2f}")
else:
    money_needed = washing_machine_price - total_money_earned
    print(f"No! {money_needed:.2f}")