number_classifications = {
    "Positive": lambda x: x >= 0,
    "Negative": lambda x: x < 0,
    "Even": lambda x: x % 2 == 0,
    "Odd": lambda x: x % 2 != 0,
}

numbers = [int(i) for i in input().split(", ")]
for classification, condition in number_classifications.items():
    print(classification, end=": ")
    print(*[i for i in numbers if condition(i)], sep=", ")