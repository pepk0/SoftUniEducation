day_of_week = input()
ticket_price = 0

if (day_of_week == "Monday" or day_of_week =="Tuesday" 
    or day_of_week == "Friday"):
    ticket_price = 12

elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    ticket_price = 14

else:
    ticket_price = 16

print(ticket_price)
