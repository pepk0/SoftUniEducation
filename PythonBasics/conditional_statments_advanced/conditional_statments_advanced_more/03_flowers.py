quantity_chrysanthemum = int(input())
quantity_rose = int(input())
quantity_tulip = int(input())
season = input()
is_holiday = input()

price_chrysanthemum = 0
price_rose = 0
price_tulip = 0
holiday_price_increase = 1.15
arrangement_price = 2
total_price_discount = 0 

if season == "Summer" or season == "Spring":
    price_chrysanthemum = 2.0
    price_rose = 4.1
    price_tulip = 2.5

elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = 3.75
    price_rose = 4.5
    price_tulip = 4.15

flower_price = (quantity_chrysanthemum * price_chrysanthemum 
                       + quantity_rose * price_rose 
                       + quantity_tulip * price_tulip)

if is_holiday == "Y":
    flower_price *= holiday_price_increase
    
if quantity_tulip > 7 and season == "Spring":
    flower_price *= 1 - 0.05

if quantity_rose >= 10 and season == "Winter":
    flower_price *= 1 - 0.1

if quantity_chrysanthemum + quantity_rose + quantity_tulip > 20:
    flower_price *= 1 - 0.2

total_bouquet_price = (flower_price * (1 - total_price_discount) 
                      + arrangement_price)

print(f"{total_bouquet_price:.2f}")
