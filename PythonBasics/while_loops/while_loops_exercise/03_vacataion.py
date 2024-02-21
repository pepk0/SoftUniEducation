money_needed = float(input())
saved_money = float(input())
days_saving = 0
days_spending = 0

while money_needed > saved_money:

    action = input()
    money = float(input())
    days_saving += 1
    
    if action == "spend":
        days_spending += 1
        if days_spending == 5:
            print("You can't save the money.", 
                  f"{days_saving}", sep="\n")
            break
        saved_money -= money
        if saved_money < 0:
            saved_money = 0
    
    elif action == "save":
        days_spending = 0
        saved_money += money

else:
    print(f"You saved the money for {days_saving} days.")   