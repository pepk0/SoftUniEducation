budget = int(input())

while True:

    command = input()
    if command == "End":
        print("You bought everything needed.")
        break

    command = float(command)    
    
    if budget - float(command) >= 0:
        budget -= command
    else:
        print("You went in overdraft!")
        break


