puzzle_price = 2.6
talking_doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
toy_truck_price = 2
more_then_fifty_toys_discount = 0.25
price_for_rent = 0.1

vacation_price = float(input())
number_puzzle = int(input())
number_talking_doll = int(input())
number_teddy_bear = int(input())
number_minion = int(input())
number_toy_truck = int(input())

number_toys = (number_puzzle + number_talking_doll + number_teddy_bear
                     + number_minion + number_toy_truck)

total_price_toys = (puzzle_price * number_puzzle +
                    number_talking_doll * talking_doll_price +
                    number_teddy_bear * teddy_bear_price +
                    number_minion * minion_price +
                    number_toy_truck * toy_truck_price)

if number_toys >= 50:
    total_price_toys *= 1 - more_then_fifty_toys_discount

money_for_rent = total_price_toys * price_for_rent
profit = total_price_toys - money_for_rent

if profit >= vacation_price:
    money_leftover = profit - vacation_price
    print(f"Yes! {money_leftover:.2f} lv left.")

else:
    money_needed = vacation_price - profit
    print(f"Not enough money! {money_needed:.2f} lv needed.")