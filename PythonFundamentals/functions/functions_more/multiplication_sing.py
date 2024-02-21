def multiplication_sing(nums: list) -> str:
    result = "positive"
    negatives = 0
    for number in nums:
        if number == 0:
            return "zero"
        elif number < 0:
            negatives += 1
    if negatives == 1 or negatives == 3:
        result = "negative"
    return result


numbers = [float(input()) for _ in range(3)]
print(multiplication_sing(numbers))
