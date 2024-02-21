numbers = int(input())
max_number = -float("inf")
sum_numbers = 0

for _ in range(numbers):

    number = int(input())

    sum_numbers += number
    if number > max_number:
        max_number = number

sum_numbers -= max_number

if max_number == sum_numbers:
    print("Yes", f"Sum = {max_number}", sep="\n")
else:
    difference = abs(max_number - sum_numbers)
    print("No", f"Diff = {difference}", sep="\n")