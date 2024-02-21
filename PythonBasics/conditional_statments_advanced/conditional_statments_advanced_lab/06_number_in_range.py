number = int(input())
answer = ""

if (-100 <= number <= 100) and number != 0:
    answer = "Yes"
else:
    answer = "No"

print(answer)