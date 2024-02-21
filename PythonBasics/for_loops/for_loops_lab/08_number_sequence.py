numbers = int(input())
minimum_number = float("inf")
maximum_number = -float("inf")

for _ in range(numbers):
    
    number = int(input())
    if number > maximum_number:
        maximum_number = number
    
    if number < minimum_number:
        minimum_number = number

print(f"Max number: {maximum_number}\nMin number: {minimum_number}")