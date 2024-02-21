employees_happiness = [int(i) for i in input().split()]
happiness_factor = int(input())
total_employees = len(employees_happiness)

improved_happiness = [i * happiness_factor for i in employees_happiness]
average_happiness = sum(improved_happiness) / total_employees
happy_employees = len(
    [el for el in improved_happiness if el >= average_happiness])

status = "Employees are not happy!"
if happy_employees >= total_employees // 2:
    status = "Employees are happy!"

print(f"Score: {happy_employees}/{total_employees}. {status}")
