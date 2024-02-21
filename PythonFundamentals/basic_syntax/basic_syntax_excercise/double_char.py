
while True:

    string = input()
    if string == "End":
        break

    elif string == "SoftUni":
        continue
    
    result = ""
    for char in string:
        result += char * 2

    print(result)