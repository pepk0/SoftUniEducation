end_range = int(input())
character_range = range(97, 97 + end_range)

for first_char in character_range:
    for second_char in character_range:
        for third_char in character_range:
            
            result = f"{chr(first_char)}{chr(second_char)}{chr(third_char)}"    
            print(result) 
