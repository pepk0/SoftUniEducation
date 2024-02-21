# list comprehension version
# 
#result = [abs(float(i)) for i in input().split()]
# print(result)

numbers = input().split()
result = []

for number in numbers:
    result.append(abs(float(number)))

print(result)
