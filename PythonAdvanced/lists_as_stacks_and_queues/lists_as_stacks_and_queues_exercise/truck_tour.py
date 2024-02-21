from collections import deque


pump_line = deque([[int(i)for i in input().split()]
                  for _ in range(int(input()))])
starting_index = 0
fuel = 0

cur_progress = pump_line.copy()

while cur_progress:

    got_fuel, distance = cur_progress.popleft()
    fuel += got_fuel

    if fuel < distance:
        starting_index += 1
        pump_line.rotate(-1)
        cur_progress = pump_line.copy()
        fuel = 0
        continue
    else:
        fuel -= distance

print(starting_index)
