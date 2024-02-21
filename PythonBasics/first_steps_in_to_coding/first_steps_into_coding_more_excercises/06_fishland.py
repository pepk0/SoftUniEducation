price_mackerel_kilogram = float(input())
price_sprat_kilogram = float(input())
bonito_kilogram = float(input())
scad_kilogram = float(input())
seashells_kilogram = int(input())

price_seashells = 7.5
price_bonito = price_mackerel_kilogram * 1.6
price_scad = price_sprat_kilogram * 1.8

total_price_bonito = bonito_kilogram * price_bonito
total_price_scad = scad_kilogram * price_scad
total_price_seashells = seashells_kilogram * price_seashells

total_sum = total_price_scad + total_price_bonito + total_price_seashells

print(f"{total_sum:.2f}")