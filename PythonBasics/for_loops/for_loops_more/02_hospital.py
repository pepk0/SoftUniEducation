number_days_for_checkups = int(input())
number_doctors = 7
people_treated = 0
people_untreated = 0 

for day in range(1, number_days_for_checkups + 1):

    patients_for_checkup = int(input())
    
    if day % 3 == 0 and people_untreated > people_treated:
        number_doctors += 1

    if patients_for_checkup <= number_doctors:
        people_treated += patients_for_checkup
    else:
        people_treated += number_doctors
        people_untreated += patients_for_checkup - number_doctors
    
print(f"Treated patients: {people_treated}.")
print(f"Untreated patients: {people_untreated}.")
