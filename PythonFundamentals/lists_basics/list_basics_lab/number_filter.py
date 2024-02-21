numbers_list = [int(input()) for _ in range(int(input()))]
command = input()

answer = [i for i in numbers_list if i % 2 == 0]

if command == "odd":
    answer = [i for i in numbers_list if i % 2 != 0]
elif command == "negative":
    answer = [i for i in numbers_list if i < 0]
elif command == "positive":
    answer = [i for i in numbers_list if i >= 0]

print(answer)
