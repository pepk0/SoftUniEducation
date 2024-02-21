def negative_vs_positive(*args) -> str:
    result = ""
    negative_sum = 0
    positive_sum = 0

    for number in args:
        number = int(number)
        if number < 0:
            negative_sum += number
        else:
            positive_sum += number

    result += f"{negative_sum}\n{positive_sum}\n"

    if abs(negative_sum) > positive_sum:
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"

    return result


print(negative_vs_positive(*(input().split())))
