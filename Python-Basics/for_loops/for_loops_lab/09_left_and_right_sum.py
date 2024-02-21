numbers = int(input())
total_numbers = numbers * 2
left_sum = 0
right_sum = 0

for number in range(1, total_numbers + 1):
    
    pair = int(input())
    
    if total_numbers / 2 < number:
        right_sum += pair
    else:
        left_sum += pair

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")