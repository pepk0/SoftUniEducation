number_months = int(input())
electricity_bill = 0
water_bill = 0 
internet_bill = 0
other_expenses = 0
total_expenses = 0

for _ in range(number_months):

    monthly_electricity = float(input())
    electricity_bill += monthly_electricity
    water_bill += 20
    internet_bill += 15
    other = ((monthly_electricity + 15 + 20) * 1.2)
    other_expenses += other    
    total_expenses += monthly_electricity + 20 + 15 + other

monthly_average = total_expenses / number_months
print(f"Electricity: {electricity_bill:.2f} lv", f"Water: {water_bill:.2f} lv",
      f"Internet: {internet_bill:.2f} lv", f"Other: {other_expenses:.2f} lv",
      f"Average: {monthly_average:.2f} lv", sep="\n") 