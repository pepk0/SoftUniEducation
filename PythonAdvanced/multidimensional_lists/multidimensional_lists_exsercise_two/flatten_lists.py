from collections import deque


lists = deque(input().split("|"))
matrix = []

while lists:
    matrix.extend([int(i) for i in lists.pop().split()])

print(*matrix, sep=" ")
