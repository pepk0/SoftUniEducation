number = float(input())
answer = ""

if number == 0:
    answer = "zero"

elif number < 0:
    if 0 < abs(number) < 1:
        answer = "small "
    elif abs(number) > 1000000:
        answer = "large "
    answer += "negative"

else:
    if 0 < abs(number) < 1:
        answer = "small "
    elif abs(number) > 1000000:
        answer = "large "
    answer += "positive"

print(answer)