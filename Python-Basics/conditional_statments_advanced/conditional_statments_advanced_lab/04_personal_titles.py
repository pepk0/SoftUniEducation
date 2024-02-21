person_age = float(input())
gender = input()
personal_title = ""

if gender == "m":
    if person_age >= 16:
        personal_title = "Mr."
    else:
        personal_title = "Master"
 
elif gender == "f":
    if person_age >= 16:
        personal_title = "Ms."
    else:
        personal_title = "Miss"

print(personal_title)
