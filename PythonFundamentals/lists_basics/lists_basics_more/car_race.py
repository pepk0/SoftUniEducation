lap_times = [int(i) for i in input().split()]

finish_point = len(lap_times) // 2
first_car_start = 0
second_car_start = len(lap_times) - 1
first_car_time = 0
second_car_time = 0

for _ in range(finish_point):
    if lap_times[first_car_start] == 0:
        first_car_time *= 0.8
    else:
        first_car_time += lap_times[first_car_start]   
    if lap_times[second_car_start] == 0:
        second_car_time *= 0.8
    else:
        second_car_time += lap_times[second_car_start]
    
    first_car_start += 1
    second_car_start -= 1

if first_car_time > second_car_time:
    wining_time = second_car_time
    wining_car = "right"
else:
    wining_time = first_car_time
    wining_car = "left"

print(f"The winner is {wining_car} with total time: {wining_time:.1f}")
