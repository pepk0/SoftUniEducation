def calculate_number(pre_letter: str, post_letter: str, number: int) -> float:
    if pre_letter.isupper():
        def pre_operation(x): return x / (ord(pre_letter) - 64)
    else:
        def pre_operation(x): return x * (ord(pre_letter) - 96)

    if post_letter.isupper():
        def post_operation(x): return x - (ord(post_letter) - 64)
    else:
        def post_operation(x): return x + (ord(post_letter) - 96)
    return post_operation(pre_operation(number))


game_elements = input().split()
result = 0
for element in game_elements:
    first_letter = element[0]
    last_letter = element[-1]
    middle_number = int(element[1:-1])
    result += calculate_number(first_letter, last_letter, middle_number)

print(f"{result:.2f}")
