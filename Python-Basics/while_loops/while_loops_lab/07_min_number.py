max_number = float("inf")
command = input()

while command != "Stop":
    
    number = int(command)
    if number < max_number:
        max_number = number
    
    command = input()
    
print(max_number)