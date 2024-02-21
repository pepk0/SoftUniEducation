start_range = int(input())
end_range = int(input())

for number in range(start_range, end_range + 1):
    is_even = False
    even_sum = 0
    odd_sum = 0
    for digit in str(number):
                
        if is_even:
            is_even = False
            even_sum += int(digit)
        else:
            is_even = True
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=" ")
