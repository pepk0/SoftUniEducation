from math import ceil, floor

magnolia_price = 3.25
price_hyacinths = 4
price_rose = 3.5
price_cactus = 8

number_magnolia = int(input())
number_hyacinths = int(input())
number_rose = int(input())
number_cactus = int(input())
price_gift = float(input())

total_price_magnolia = number_magnolia * magnolia_price
total_price_hyacinths = number_hyacinths * price_hyacinths
total_price_rose = number_rose * price_rose
total_price_cactus = number_cactus * price_cactus

order_price = (total_price_magnolia + total_price_hyacinths 
                    + total_price_rose + total_price_cactus)

order_tax = order_price * 0.05
total_profit = order_price - order_tax

if price_gift <= total_profit:

    money_left_over = floor(total_profit - price_gift)
    print(f"She is left with {money_left_over} leva.")

else:

    money_to_borrow = ceil(price_gift - total_profit)
    print(f"She will have to borrow {money_to_borrow} leva.")