from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"ElbowPad": ElbowPad, "KneePad": KneePad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value.isalnum():
            raise ValueError(
                "Tournament name should contain letters and digits only!")
        self.__name = value

    @staticmethod
    def get_team_points(team) -> int:
        return team.advantage + sum(x.protection for x in team.equipment)

    def get_last_equipment_by_type(self, equipment_type):
        collection = [eq for eq in self.equipment if
                      eq.__class__.__name__ == equipment_type]
        return collection[-1] if collection else None

    def get_team_by_name(self, team_name):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None

    def add_equipment(self, equipment_type: str) -> str:
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        equipment_item = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment_item)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str,
                 advantage: int) -> str:
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str) -> str:
        team: BaseTeam = self.get_team_by_name(team_name)
        equipment: BaseEquipment = self.get_last_equipment_by_type(
            equipment_type)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.remove(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str) -> str:
        team = self.get_team_by_name(team_name)

        if not team:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(
                f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str) -> str:
        changed = 0
        for item in self.equipment:
            if item.__class__.__name__ == equipment_type:
                item.increase_price()
                changed += 1

        return f"Successfully changed {changed}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1: BaseTeam = self.get_team_by_name(team_name1)
        team2: BaseTeam = self.get_team_by_name(team_name2)

        if not team1.__class__.__name__ == team2.__class__.__name__:
            raise Exception(f"Game cannot start! Team types mismatch!")

        team1_points = self.get_team_points(team1)
        team2_points = self.get_team_points(team2)

        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team1.name}."
        if team1_points < team2_points:
            team2.win()
            return f"The winner is {team2.name}."
        return "No winner in this game."

    def get_statistics(self) -> str:
        team_statistics = [team.get_statistics() for team in
                           sorted(self.teams, key=lambda x: -x.wins)]

        result = (f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\nTeams:")
        for team_stats in team_statistics:
            result += f"\n{team_stats}"

        return result
