number_1 = int(input())
number_2 = int(input())
operator = input()

number = "" # even or odd
result = 0

if operator == "+":
    result = number_1 + number_2

elif operator == "-":
    result = number_1 - number_2

elif operator == "*":
    result = number_1 * number_2

elif operator == "/" and (number_2 != 0 and number_1 != 0):
    result = number_1 / number_2

elif operator == "%" and (number_2 != 0 and number_1 != 0):
    result = number_1 % number_2


if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        number = "even"
    else:
        number = "odd"
    print(f"{number_1} {operator} {number_2} = {result} - {number}")

elif operator == "/" or operator == "%":
    if number_2 == 0:
        print(f"Cannot divide {number_2} by zero")
    elif operator == "/":
        print(f"{number_1} {operator} {number_2} = {result:.2f}")
    elif operator == "%":
        print(f"{number_1} {operator} {number_2} = {result}")
