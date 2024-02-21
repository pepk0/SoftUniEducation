foil_price = 1.5
paint_price = 14.5
paint_thinner_price = 5.0
bag_price = 0.4

quantity_foil = int(input())
liters_paint = int(input())
quantity_paint_thinner = int(input())
time_of_work = int(input())

# adding extra 2square meters to the foil and 10% extra paint
quantity_foil += 2
liters_paint += liters_paint * 0.1

material_price = quantity_foil * foil_price + liters_paint * paint_price \
               + quantity_paint_thinner * paint_thinner_price + bag_price

service_cost = (material_price * 0.3) * time_of_work

full_price = material_price + service_cost

print(full_price)