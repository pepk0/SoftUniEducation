from project.player import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: list = []

    def assign_player(self, player_: Player) -> str:
        if player_ not in self.players:

            if player_.guild == "Unaffiliated":
                self.players.append(player_)
                player_.guild = self.name
                return f"Welcome player {player_.name} to the guild {self.name}"
            else:
                return f"Player {player_.name} is in another guild."

        return f"Player {player_.name} is already in the guild."

    def kick_player(self, player_name: str) -> str:
        if player_name in self.players:
            self.players[self.players.index(player_name)].guild = "Unaffiliated"
            self.players.remove(player_name)
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        players = "\n".join(player_.player_info() for player_ in self.players)
        return f"Guild: {self.name}\n{players}"


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
