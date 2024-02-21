number_of_symbols = int(input())
next_bracket = "("
balanced = True

for _ in range(number_of_symbols):

    symbol = input()

    if symbol == "(" or symbol == ")":
        if symbol != next_bracket:
            balanced = False
            break
        else:
            if next_bracket == "(":
                next_bracket = ")"
            else:
                next_bracket = "("

print("BALANCED" if balanced else "UNBALANCED")
