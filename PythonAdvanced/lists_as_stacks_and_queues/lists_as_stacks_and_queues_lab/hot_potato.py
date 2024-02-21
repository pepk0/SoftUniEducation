from collections import deque


kids = deque(input().split())
rotations = int(input())

while len(kids) > 1:
    kids.rotate(-(rotations - 1))
    removed_kid = kids.popleft()
    print(f"Removed {removed_kid}")
else:
    print(f"Last is {kids.popleft()}")
