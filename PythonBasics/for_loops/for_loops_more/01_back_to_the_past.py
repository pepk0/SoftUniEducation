inherited_money = float(input())
year_to_live_to = int(input())
person_age = 17
money_needed = 0

for year in range(1800, year_to_live_to + 1):
    person_age += 1
    
    if year % 2 == 0:
        money_needed += 12000
    else:
        money_needed += 12000 + 50 * person_age

difference = abs(money_needed - inherited_money)

if inherited_money >= money_needed:
    print(f"Yes! He will live a carefree life and will "
          f"have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")
