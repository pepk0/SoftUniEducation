number_of_cargos = int(input())
van_transport = 0
truck_transport = 0
train_transport = 0
tons_cargo_transported = 0
total_price = 0

for _ in range(number_of_cargos):

    tons_cargo = int(input())

    if tons_cargo <= 3:
        van_transport += tons_cargo
        total_price += tons_cargo * 200

    elif 4 <= tons_cargo <= 11:
        truck_transport += tons_cargo
        total_price += tons_cargo * 175
    
    else:
        train_transport += tons_cargo
        total_price += tons_cargo * 120

    tons_cargo_transported += tons_cargo

average_price_per_ton = total_price / tons_cargo_transported 
percent_van = (van_transport / tons_cargo_transported) * 100
percent_truck = (truck_transport / tons_cargo_transported) * 100
percent_train = (train_transport / tons_cargo_transported) * 100

print(f"{average_price_per_ton:.2f}", f"{percent_van:.2f}%", 
      f"{percent_truck:.2f}%", f"{percent_train:.2f}%", sep="\n")
