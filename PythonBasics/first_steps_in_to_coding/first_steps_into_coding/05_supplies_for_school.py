pen_price = 5.80
marker_price = 7.2
cleaning_solution = 1.2

quantity_pen = int(input())
quantity_marker = int(input())
liters_cleaning_solution = int(input())
percent_discount = int(input()) / 100

total_price_pen = quantity_pen * pen_price
total_price_marker = quantity_marker * marker_price
total_price_cleaning_solution =  liters_cleaning_solution * cleaning_solution

price = (total_price_cleaning_solution + total_price_marker \
            + total_price_pen)

price -= price * percent_discount

print(price)