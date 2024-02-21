stadium_capacity = int(input())
number_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for _ in range(number_fans):

    fan_sector = input()
    
    if fan_sector == "A":
        sector_a += 1
    
    elif fan_sector == "B":
        sector_b += 1 

    elif fan_sector == "V":
        sector_v += 1 

    elif fan_sector == "G":
        sector_g += 1 

percent_total_fans = (number_fans / stadium_capacity) * 100
percent_sector_a = (sector_a / number_fans) * 100
percent_sector_b = (sector_b / number_fans) * 100
percent_sector_v = (sector_v / number_fans) * 100
percent_sector_g = (sector_g / number_fans) * 100

print(f"{percent_sector_a:.2f}%", f"{percent_sector_b:.2f}%", 
      f"{percent_sector_v:.2f}%", f"{percent_sector_g:.2f}%",
      f"{percent_total_fans:.2f}%", sep="\n")