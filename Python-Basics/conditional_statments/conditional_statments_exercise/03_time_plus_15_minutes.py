extra_minutes = 15

hour = int(input())
minutes = int(input())

total_minutes = hour * 60 + minutes + extra_minutes

new_time_hours = total_minutes // 60
new_time_minutes = total_minutes % 60

if new_time_hours >= 24:
    new_time_hours = 0

print(f"{new_time_hours}:{new_time_minutes:02d}")
