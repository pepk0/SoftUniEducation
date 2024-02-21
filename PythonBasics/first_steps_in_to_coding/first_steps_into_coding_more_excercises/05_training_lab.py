row_length = 120
desk_width = 70

room_length = float(input()) * 100 # values in cm 
room_width = float(input()) * 100

room_width -= 100 # 100 cm are taken up by the hall

number_desks = room_width // desk_width
number_rows = room_length // row_length

total_places = number_desks * number_rows - 3 # 2 spaces and 1 space taken up

print(int(total_places))