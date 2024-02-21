EURO_COURSE = 1.94

price_vegetables = float(input())
price_fruits = float(input())
total_kilograms_vegetables = int(input())
total_kilograms_fruits = int(input())

total_price_leva = total_kilograms_vegetables * price_vegetables \
                 + total_kilograms_fruits * price_fruits

total_price_euro = total_price_leva / EURO_COURSE

print(f"{total_price_euro:.2f}")