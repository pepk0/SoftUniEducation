from math import floor, ceil

vineyard_square_meters = int(input())
kg_grape_square_meter = float(input())
liters_wine_needed = int(input())
number_personnel = int(input())

total_grape_harvest = vineyard_square_meters * kg_grape_square_meter
total_wine_produced = total_grape_harvest * 0.4 / 2.5

if liters_wine_needed > total_wine_produced:
    more_wine_needed = floor(liters_wine_needed - total_wine_produced) 
    print(f"It will be a tough winter! More {more_wine_needed}"
          " liters wine needed.")
else:
    leftover_wine = ceil(total_wine_produced - liters_wine_needed)
    wine_for_worker = 0
    
    if leftover_wine > 0:
        wine_for_worker = ceil(leftover_wine / number_personnel)
    
    print(f"Good harvest this year! Total wine: {floor(total_wine_produced)}"
          " liters.")
    print(f"{leftover_wine} liters left -> {wine_for_worker}"
          " liters per person.")