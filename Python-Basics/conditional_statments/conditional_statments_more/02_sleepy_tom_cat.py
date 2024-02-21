days_in_year = 365
minutes_cat_needs_to_sleep = 30000

number_of_days_off = int(input())

number_working_days = days_in_year - number_of_days_off
time_cat_plays = (number_of_days_off * 127 + number_working_days * 63)
time_cat_slept = minutes_cat_needs_to_sleep - time_cat_plays

if minutes_cat_needs_to_sleep > time_cat_plays:
    print("Tom sleeps well")
    print(f"{time_cat_slept // 60} hours and {time_cat_slept % 60}"
          " minutes less for play")
else:
    time_cat_slept = abs(time_cat_slept)
    print("Tom will run away")
    print(f"{time_cat_slept // 60} hours and {time_cat_slept % 60}"
          " minutes more for play")