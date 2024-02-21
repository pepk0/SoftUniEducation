vip_ticket_price = 499.99
normal_ticket_price = 249.99
percent_transport = 0

budget = float(input())
ticket_category = input()
number_of_people = int(input())

if 1 <= number_of_people <= 4:
    percent_transport = 0.75

elif 5 <= number_of_people <= 9:
    percent_transport = 0.6

elif 10 <= number_of_people <= 24:
    percent_transport = 0.5

elif 25 <= number_of_people <= 49:
    percent_transport = 0.4

elif number_of_people > 50:
    percent_transport = 0.25

if ticket_category == "VIP":
    ticket_price = vip_ticket_price

else:
    ticket_price = normal_ticket_price

money_left = budget * (1 - percent_transport)
total_ticket_price = number_of_people * ticket_price

if money_left >= total_ticket_price:
    money_leftover = money_left - total_ticket_price 
    print(f"Yes! You have {money_leftover:.2f} leva left.")

else:
    money_needed = total_ticket_price - money_left
    print(f"Not enough money! You need {money_needed:.2f} leva.")
    