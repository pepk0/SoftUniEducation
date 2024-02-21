start_range = int(input())
end_range = int(input())
magic_number = int(input())
number_found = False
total_iterations = 0
combination_number_one = 0
combination_number_two = 0

for first_number in range(start_range, end_range + 1):
    for second_number in range(start_range, end_range + 1):
        total_iterations += 1
        current_sum = first_number + second_number
        
        if current_sum == magic_number:
            combination_number_one = first_number                        
            combination_number_two = second_number                        
            number_found = True
            break
        
    if number_found:
            break

if number_found:
    print(f"Combination N:{total_iterations} ({combination_number_one} "
          f"+ {combination_number_two} = {magic_number})") 
else:
    print(f"{total_iterations} combinations - neither equals {magic_number}")