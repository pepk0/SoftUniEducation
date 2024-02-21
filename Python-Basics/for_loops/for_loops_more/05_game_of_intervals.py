number_moves = int(input())
total_points = 0
zero_to_nine = 0
ten_to_nineteen = 0
twenty_to_twentynine = 0
thirty_to_thirtynine = 0
forty_to_fifty = 0
invalid_numbers = 0

for _ in range(number_moves):

    score = int(input())

    if score < 0 or score > 50:
        total_points /= 2
        invalid_numbers += 1

    elif score <= 9:
        zero_to_nine += 1
        total_points += score * 0.2
    
    elif 10 <= score <= 19:
        ten_to_nineteen += 1
        total_points += score * 0.3
    
    elif 20 <= score <= 29:
        twenty_to_twentynine += 1
        total_points += score * 0.4
    
    elif 30 <= score <= 39:
        thirty_to_thirtynine += 1
        total_points += 50
    
    else:
        forty_to_fifty += 1
        total_points += 100

percent_zero_to_nine = (zero_to_nine / number_moves) * 100
percent_ten_to_nineteen = (ten_to_nineteen / number_moves) * 100
percent_twenty_to_twentynine = (twenty_to_twentynine / number_moves) * 100
percent_thirty_to_thirtynine = (thirty_to_thirtynine / number_moves) * 100
percent_forty_to_fifty = (forty_to_fifty / number_moves) * 100
percent_invalid = (invalid_numbers / number_moves) * 100

print(f"{total_points:.2f}", f"From 0 to 9: {percent_zero_to_nine:.2f}%",
      f"From 10 to 19: {percent_ten_to_nineteen:.2f}%",
      f"From 20 to 29: {percent_twenty_to_twentynine:.2f}%",
      f"From 30 to 39: {percent_thirty_to_thirtynine:.2f}%",
      f"From 40 to 50: {percent_forty_to_fifty:.2f}%",
      f"Invalid numbers: {percent_invalid:.2f}%", sep="\n")
