number = int(input())
modifier = 1

for i in range(1, (number * 2)):

    print("*" * modifier)
    
    if i < number:
        modifier += 1
    else:
        modifier -= 1