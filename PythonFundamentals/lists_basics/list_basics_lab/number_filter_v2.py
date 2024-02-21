numbers_list = [int(input()) for _ in range(int(input()))]
command = input()

options = {

    "even": lambda x: x % 2 == 0,
    "odd": lambda x: x % 2 != 0,
    "positive": lambda x: x >= 0,
    "negative": lambda x: x < 0,
}

condition = options[command]
result = [x for x in numbers_list if condition(x)]
print(result)
