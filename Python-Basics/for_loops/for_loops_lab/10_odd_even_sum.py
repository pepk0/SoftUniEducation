numbers = int(input())
even_sum = 0
odd_sum = 0

for num in range(1, numbers + 1):

    input_number = int(input())

    if num % 2 == 0:
        even_sum += input_number
    else:
        odd_sum += input_number

if even_sum == odd_sum:
    print("Yes", f"Sum = {even_sum}", sep="\n")
else:
    difference = abs(even_sum - odd_sum)
    print("No", f"Diff = {difference}", sep="\n")