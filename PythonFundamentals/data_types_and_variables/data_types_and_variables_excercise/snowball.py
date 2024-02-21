number_snowballs = int(input())
best_snowball = 0 
result = ""

for _ in range(number_snowballs):

    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_rating = (snowball_weight / snowball_time) ** snowball_quality
    
    if snowball_rating >= best_snowball:
        best_snowball = snowball_rating
        result = (f"{snowball_weight} : {snowball_time} = {int(best_snowball)} "
                  f"({snowball_quality})")

print(result)
