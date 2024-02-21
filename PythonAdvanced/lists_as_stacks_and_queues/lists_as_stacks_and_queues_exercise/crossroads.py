from collections import deque


green_light = int(input())
free_window = int(input())
car_lane = deque()
passed_cars = 0
crash = False

command = input()

while command != "END":
    if command == "green":
        cur_green_light = green_light
        cur_free_window = free_window
        
        while car_lane and cur_green_light > 0:
            car = car_lane.popleft()

            cur_total = cur_green_light + cur_free_window
            
            if len(car) > cur_total:
                cur_green_light = 0
                crash = True
                char_hit = car[cur_total]
            
                print("A crash happened!",
                      f"{car} was hit at {char_hit}.", sep="\n")
                continue
            
            cur_green_light -= len(car)
            passed_cars += 1
    else:
        car_lane.append(command)

    if crash:
        break

    command = input()
else:
    print("Everyone is safe.",
          f"{passed_cars} total cars passed the crossroads.", sep="\n")
