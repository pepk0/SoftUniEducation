type_fuel = input()
fuel_in_tank = float(input())

type_of_fuels = ["Diesel", "Gasoline", "Gas"]

if type_fuel in type_of_fuels:
    
    if fuel_in_tank >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    else:
        print(f"Fill your tank with {type_fuel.lower()}!")

else:
    print("Invalid fuel!")