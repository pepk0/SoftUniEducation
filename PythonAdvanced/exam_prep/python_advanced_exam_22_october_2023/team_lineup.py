def team_lineup(*player_info) -> str:
    teams_and_players = {}
    result_string = []

    for player, team in player_info:
        if team not in teams_and_players:
            teams_and_players[team] = []
        teams_and_players[team].append(player)

    for team, players in sorted(teams_and_players.items(),
                                key=lambda x: (-len(x[1]), x[0])):
        result_string.append(f"{team}:")
        [result_string.append(f"  -{el}") for el in players]

    return "\n".join(result_string)
