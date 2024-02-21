number_tabs = int(input())
salary = int(input())

for _ in range(number_tabs):

    site_on_tab = input()

    if site_on_tab == "Facebook":
        salary -= 150

    elif site_on_tab == "Instagram":
        salary -= 100
    
    elif site_on_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

else:
    print(salary)
