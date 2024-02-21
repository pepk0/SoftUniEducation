from math import ceil


time_for_eating = 0.125 # 1/8
time_for_relaxing = 0.25 # 1/4 

tv_series_name = input()
episode_length = int(input())
break_length = int(input())

eating_time = break_length * time_for_eating
relaxing_time = break_length * time_for_relaxing

free_time_for_watching = break_length - (eating_time + relaxing_time)

if free_time_for_watching >= episode_length:
    time_left = ceil(free_time_for_watching - episode_length)
    print(f"You have enough time to watch {tv_series_name} and left "
          f"with {time_left} minutes free time.")
    
else:
    more_time_needed = ceil(episode_length - free_time_for_watching)
    print(f"You don't have enough time to watch {tv_series_name}, you need"
          f" {more_time_needed} more minutes.")
