# def repeat_string(string: str, num: int) -> str:
#     return string * num


# string = input()
# number = int(input())

# print(repeat_string(string, number))

string = input()
number = int(input())

result = lambda s, n: s * n
print(result(string, number))
