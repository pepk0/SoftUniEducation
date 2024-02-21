while True:

    student = input()
    if student == "Voldemort":
        print("You must not speak of that name!")
        break
    
    elif student == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    
    house = ""
    if len(student) < 5:
        house = f"{student} goes to Gryffindor."

    elif len(student) == 5:
        house = f"{student} goes to Slytherin."

    elif len(student) == 6:
        house = f"{student} goes to Ravenclaw."

    else: #elif len(student) == 6:
        house = f"{student} goes to Hufflepuff."

    print(house)
