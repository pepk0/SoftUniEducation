last_sector = input()
rows_in_first_sector = int(input())
number_odd_seats = int(input())
sector_range = range(ord("A"), ord(last_sector) + 1)
odd_range = range(97, 97 + number_odd_seats)
even_range = range(97, 97 + number_odd_seats + 2)
total_seats = 0

for sector in sector_range:
    for row in range(1, rows_in_first_sector + 1):
        range_to_use = odd_range
        if row % 2 == 0:
            range_to_use = even_range
        for seat in range_to_use: 
            
            print(f"{chr(sector)}{row}{chr(seat)}")
            total_seats += 1        
    
    rows_in_first_sector += 1

print(total_seats)
