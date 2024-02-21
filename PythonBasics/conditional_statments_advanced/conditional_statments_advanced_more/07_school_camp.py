season = input()
type_of_group = input()
number_students = int(input())
number_nights_stayed = int(input())

discount = 0
sport = ""
price_per_night = 0

if type_of_group == "boys" or type_of_group == "girls":
    if season == "Winter":
        price_per_night = 9.6
        if type_of_group == "girls":
            sport = "Gymnastics"
        else:
            sport = "Judo"
    elif season == "Spring":
        price_per_night = 7.2
        if type_of_group == "girls":
            sport = "Athletics"
        else:
            sport = "Tennis"
    elif season == "Summer":
        price_per_night = 15
        if type_of_group == "girls":
            sport = "Volleyball"
        else:
            sport = "Football"

elif type_of_group == "mixed":
    if season == "Winter":
        price_per_night = 10
        sport = "Ski"
    elif season == "Spring":
        price_per_night = 9.5
        sport = "Cycling"
    elif season == "Summer":
        price_per_night = 20
        sport = "Swimming"

if 10 <= number_students < 20:
    discount = 0.05

elif 20 <= number_students < 50:
    discount = 0.15

elif number_students >= 50:
    discount = 0.5

total_price = (number_nights_stayed * price_per_night * number_students
                * (1 - discount))

print(f"{sport} {total_price:.2f} lv.")
