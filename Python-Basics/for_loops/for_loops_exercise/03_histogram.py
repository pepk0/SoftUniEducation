numbers = int(input())
num_lower_200 = 0
num_between_200_and_399 = 0
num_between_400_and_599 = 0
num_between_600_and_799 = 0
num_above_800 = 0

for _ in range(numbers):

    number = int(input())

    if number < 200:
        num_lower_200 += 1
    
    elif 200 <= number <= 399:
        num_between_200_and_399 += 1
    
    elif 400 <= number <= 599:
        num_between_400_and_599 += 1
    
    elif 600 <= number <= 799:
        num_between_600_and_799 += 1

    else:
        num_above_800 += 1

num_lower_200 = (num_lower_200 / numbers) * 100
num_between_200_and_399 = (num_between_200_and_399 / numbers) * 100
num_between_400_and_599 = (num_between_400_and_599 / numbers) * 100
num_between_600_and_799 = (num_between_600_and_799 / numbers) * 100
num_above_800 = (num_above_800 / numbers) * 100

print(f"{num_lower_200:.2f}%", f"{num_between_200_and_399:.2f}%", 
      f"{num_between_400_and_599:.2f}%", f"{num_between_600_and_799:.2f}%", 
      f"{num_above_800:.2f}%", sep="\n")
