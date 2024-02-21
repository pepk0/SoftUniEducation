iterations = int(input())

for _ in range(iterations):

    string = input()

    condition_one = "." not in string
    condition_two = "," not in string
    condition_three = "_" not in string

    result = f"{string} is not pure!"
    if condition_one and condition_two and condition_three:
        result = f"{string} is pure."

    print(result)
