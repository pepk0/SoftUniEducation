def check_valid_paren(str_parentheses: str) -> str:
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
  
    if len(str_parentheses) % 2 != 0:
        return "NO"
  
    for parentheses in str_parentheses:
        if parentheses not in mapping:
            stack.append(parentheses)
        else:
            prev_parentheses = stack.pop()
            if prev_parentheses != mapping[parentheses]:
                return "NO"
  
    return "YES"


parentheses = input()
print(check_valid_paren(parentheses))
