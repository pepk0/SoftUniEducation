# result = [round(float(i)) for i in input().split()]
# print(result)

numbers = input().split()
result = []

for number in numbers:
    result.append(round(float(number)))

print(result)
