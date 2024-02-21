string = input()
strength = 0
result = ""

for index in range(len(string)):
    if strength and string[index] != ">":
        strength -= 1
    elif string[index] == ">":
        result += string[index]
        strength += int(string[index + 1])
    else:
        result += string[index]

print(result)
