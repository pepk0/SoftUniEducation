price_gas_liter = 0.93
price_gasoline_liter = 2.22
price_diesel_liter = 2.33

type_fuel = input()
amount_fuel = float(input())
discount_card = input()

total_price = 0

if type_fuel == "Gas":
    
    if discount_card == "Yes":
        price_gas_liter -= 0.08
    total_price = amount_fuel * price_gas_liter
    
elif type_fuel == "Gasoline":
        
    if discount_card == "Yes":
        price_gasoline_liter -= 0.18
    total_price = amount_fuel * price_gasoline_liter
    
elif type_fuel == "Diesel":
        
    if discount_card == "Yes":
        price_diesel_liter -= 0.12
    total_price = amount_fuel * price_diesel_liter

if amount_fuel >= 20 and amount_fuel <= 25:
      
    total_price *= (1 - 0.08)

elif amount_fuel > 25:
      
    total_price *= (1 - 0.1)

print(f"{total_price:.2f} lv.")