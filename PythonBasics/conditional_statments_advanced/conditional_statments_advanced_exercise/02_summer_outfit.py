whether_celsius = int(input())
time_of_day = input()

shoes = ""
outfit = ""

if time_of_day == "Morning":
    if 10 <= whether_celsius <= 18:
        outfit = "Sweatshirt" 
        shoes = "Sneakers"
    elif 18 < whether_celsius <= 24:
        outfit = "Shirt" 
        shoes = "Moccasins"
    elif whether_celsius >= 25:
        outfit = "T-Shirt" 
        shoes = "Sandals"

elif time_of_day == "Afternoon":
    if 10 <= whether_celsius <= 18:
        outfit = "Shirt" 
        shoes = "Moccasins"
    elif 18 < whether_celsius <= 24:
        outfit = "T-Shirt" 
        shoes = "Sandals"
    elif whether_celsius >= 25:
        outfit = "Swim Suit" 
        shoes = "Barefoot"

elif time_of_day == "Evening":
        outfit = "Shirt" 
        shoes = "Moccasins"

print(f"It's {whether_celsius} degrees, get your {outfit} and {shoes}.")
