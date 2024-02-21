pool_volume = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
hours_worker_is_absent = float(input())

first_pipe_work_rate = first_pipe_flow * hours_worker_is_absent
second_pipe_work_rate = second_pipe_flow * hours_worker_is_absent

water_pumped = first_pipe_work_rate + second_pipe_work_rate

if pool_volume >= water_pumped:
    
    pool_percent_full = (water_pumped / pool_volume) * 100
    percent_first_pipe_pumped = (first_pipe_work_rate / water_pumped) * 100
    percent_second_pipe_pumped = (second_pipe_work_rate / water_pumped) * 100
    
    print(f"The pool is {pool_percent_full:.2f}% full. "
          f"Pipe 1: {percent_first_pipe_pumped:.2f}%. "
          f"Pipe 2: {percent_second_pipe_pumped:.2f}%.")

else:
    pool_overfill = water_pumped - pool_volume

    print(f"For {hours_worker_is_absent} hours the pool overflows"
          f"with {pool_overfill:.2f} liters")