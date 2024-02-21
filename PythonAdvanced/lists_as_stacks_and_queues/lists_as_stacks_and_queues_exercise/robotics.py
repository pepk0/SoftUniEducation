from collections import deque
from datetime import timedelta, datetime


worker_robots = {}

for robot in input().split(";"):
    name, workload = robot.split("-")
    worker_robots[name] = [int(workload), 0]
factory_starting_time = datetime.strptime(input(), "%H:%M:%S")

seconds_passed = 0
product_line = deque()

while True:
    command = input()
    if command == "End":
        break
    product_line.append(command)

while product_line:
    seconds_passed += 1
    product = product_line.popleft()

    free_workers = []
    
    for worker in worker_robots:
        if worker_robots[worker][1]:
            worker_robots[worker][1] -= 1
        if worker_robots[worker][1] == 0:
            free_workers.append(worker)

    if free_workers:
        time = factory_starting_time + timedelta(seconds=seconds_passed)
        time = datetime.strftime(time, "%H:%M:%S")
        worker_robots[free_workers[0]][1] = worker_robots[free_workers[0]][0]
        print(f"{free_workers[0]} - {product} [{time}]")
    else:
        product_line.append(product)
