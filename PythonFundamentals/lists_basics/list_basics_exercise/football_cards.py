booked_players = [el for el in input().split()]
team_a = [f"A-{i}" for i in range(1, 12)]
team_b = [f"B-{i}" for i in range(1, 12)]
terminated_game = False

for player in booked_players:
    
    if player in team_a or player in team_b:
        if player[0] == "A":
            team_a.remove(player)
        else:
            team_b.remove(player)
    
    length_team_a = len(team_a)
    length_team_b = len(team_b)

    if length_team_a < 7 or length_team_b < 7:
        terminated_game = True
        break

print(f"Team A - {length_team_a};", f"Team B - {length_team_b}", sep=" ")
if terminated_game:
    print("Game was terminated")
