actor_name =  input()
academy_points = float(input())
number_of_judges = int(input())
awarded_points = academy_points

for _ in range(number_of_judges):

    judge = input()
    points = float(input())

    awarded_points += len(judge) * points / 2

    if awarded_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for "
              f"leading role with {awarded_points:.1f}!")
        break
else:
    points_needed = 1250.5 - awarded_points
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")