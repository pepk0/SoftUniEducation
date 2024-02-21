def add_player(name: str, position: str, skill: int, players: dict) -> None:
    if name not in players:
        players[name] = {}
    if position not in players[name]:
        players[name][position] = skill
    else:
        if players[name][position] <= skill:
            players[name][position] = skill


def battle(player: str, other: str, players: dict) -> None:
    if player not in players or other not in players:
        return
    for position_player, skill_player in players[player].items():
        for position_other, skill_other in players[other].items():
            if position_other == position_player:
                if skill_player == skill_other:
                    return
                elif skill_player > skill_other:
                    players.pop(other)
                    return
                elif skill_player < skill_other:
                    players.pop(player)
                    return


player_pool = {}
while True:
    command = input()
    if "vs" in command:
        player_one, player_two = command.split(" vs ")
        battle(player_one, player_two, player_pool)
    elif "->" in command:
        player_name, position_name, skill = command.split(" -> ")
        add_player(player_name, position_name, int(skill), player_pool)
    else:
        break

for player, skills in sorted(player_pool.items(), 
                             key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(skills.values())} skill")
    for position, skill in sorted(skills.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
