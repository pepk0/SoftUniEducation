from collections import deque


bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(i) for i in input().split()])
locks = deque([int(i) for i in input().split()])
intelligence_value = int(input())
cur_barrel_load = gun_barrel_size

while bullets and locks:
    lock = locks.popleft()
    bullet = bullets.pop()
    intelligence_value -= bullet_price
    cur_barrel_load -= 1

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    if not cur_barrel_load and bullets:
        print("Reloading!")
        if len(bullets) < gun_barrel_size:
            cur_barrel_load += len(bullets)
        else:
            cur_barrel_load = gun_barrel_size

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${int(intelligence_value)}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
