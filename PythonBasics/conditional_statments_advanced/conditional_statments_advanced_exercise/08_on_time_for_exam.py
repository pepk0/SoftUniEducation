exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_minutes = exam_hour * 60 + exam_minute
arrival_time_minutes = arrival_hour * 60 + arrival_minute

difference = abs(exam_time_minutes - arrival_time_minutes)
hour = difference // 60
minute = difference % 60

if exam_time_minutes < arrival_time_minutes:
    print("Late")
    if difference >= 60:
        print(f"{hour}:{minute:02d} hours after the start")
    else:
        print(f"{minute} minutes after the start")

elif exam_time_minutes > arrival_time_minutes:
    if difference <= 30:
        print("On time")
    else:
        print("Early")
    if difference >= 60:
        print(f"{hour}:{minute:02d} hours before the start")
    else:
        print(f"{minute} minutes before the start")

else:
    print("On time")
 