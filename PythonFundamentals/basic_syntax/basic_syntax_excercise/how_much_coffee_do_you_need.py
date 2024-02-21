coffee = 0

while True:

    command = input()
    if command == "END":
        break
    
    condition_one = command.lower() == "cat" or command.lower() == "dog"
    condition_two = command.lower() == "coding"
    condition_three = command.lower() == "movie"
    
    if condition_one or condition_two or condition_three:
        if command.islower():
            coffee += 1
        else:
            coffee += 2

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)