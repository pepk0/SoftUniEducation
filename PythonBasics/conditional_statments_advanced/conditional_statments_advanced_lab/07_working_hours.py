hour = int(input())
day_of_week = input()
store_status = ""

if day_of_week != "Sunday" and 10 <= hour <= 18:
    store_status = "open"
else:
    store_status = "closed"

print(store_status)
