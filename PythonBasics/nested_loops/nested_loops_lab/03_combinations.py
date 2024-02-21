target_number = int(input())
valid_combination = 0 

for first_number in range(target_number + 1):
    for second_number in range(target_number + 1):
        for third_number in range(target_number + 1):
            if first_number + second_number + third_number == target_number:
                valid_combination += 1

print(valid_combination)