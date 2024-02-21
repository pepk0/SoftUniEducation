from collections import deque


rows, cols = [int(i) for i in input().split()]
snake = deque(input())

for row in range(1, rows + 1):
    phrase = ""
    for col in range(cols):

        letter = snake.popleft()
        phrase += letter
        snake.append(letter)

    print(phrase if row % 2 != 0 else phrase[::-1])
