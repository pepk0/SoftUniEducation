current_record = float(input())
swimming_distance = float(input())
swimming_speed = float(input())

# we calculate the water resistance
# every 15 meter 12.5 seconds are added to the total time
time_added_by_resistance = (swimming_distance // 15 
                            * 12.5)

swim_time = swimming_speed * swimming_distance + time_added_by_resistance

if current_record > swim_time:
    print(f"Yes, he succeeded! The new world record is "
          f"{swim_time:.2f} seconds.")

else:
    time_above_record = swim_time - current_record
    print(f"No, he failed! He was {time_above_record:.2f} seconds slower.")