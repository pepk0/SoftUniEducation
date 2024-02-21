day = input()
type_of_day = ""

if (day == "Monday" or day == "Tuesday" or day == "Wednesday"
    or day == "Thursday" or day == "Friday"):
    type_of_day = "Working day"

elif day == "Saturday" or day == "Sunday":
    type_of_day = "Weekend"

else:
    type_of_day = "Error"

print(type_of_day)