tournaments_competed_in = int(input())
starting_points = int(input())
points_won = 0
tournaments_won = 0

for _ in range(tournaments_competed_in):

    tournament_results = input()

    if tournament_results == "W":
        points_won += 2000
        tournaments_won += 1    
    
    elif tournament_results == "F":
        points_won += 1200

    elif tournament_results == "SF":
        points_won += 720

total_points = points_won + starting_points
average_points = int(points_won / tournaments_competed_in)
win_percent = (tournaments_won / tournaments_competed_in) * 100

print(f"Final points: {total_points}", f"Average points: {average_points}",
      f"{win_percent:.2f}%", sep="\n")