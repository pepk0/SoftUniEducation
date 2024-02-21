from collections import deque


total_food = int(input())
food_queue = deque([int(i) for i in input().split()])

print(max(food_queue))

while food_queue:
    current_order = food_queue.popleft()

    if current_order > total_food:
        food_queue.appendleft(current_order)
        break
    else:
        total_food -= current_order

print("Orders complete" if not food_queue
      else "Orders left:", *food_queue, sep=" ")
