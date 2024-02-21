number_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

hour_per_day = int(number_pages / number_of_days) // pages_per_hour

print(hour_per_day)