from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_BREEDS = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self) -> None:
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def find_horse_by_name(self, horse_name: str):
        try:
            return [x for x in self.horses if x.name == horse_name][0]
        except IndexError:
            return None

    def find_jockey_by_name(self, jockey_name: str):
        try:
            return [x for x in self.jockeys if x.name == jockey_name][0]
        except IndexError:
            return None

    def find_race_by_type(self, race_type: str):
        try:
            return [x for x in self.horse_races if x.race_type == race_type][0]
        except IndexError:
            return None

    def find_last_horse_of_type(self, horse_type: str):
        try:
            return [h for h in self.horses if h.__class__.__name__ ==
                    horse_type and not h.is_taken][-1]
        except IndexError:
            return None

    @staticmethod
    def find_winner(jockeys: List[Jockey]) -> Jockey:
        max_speed = float("-inf")
        winner = None
        for jockey in jockeys:
            if jockey.horse.speed > max_speed:
                winner = jockey
                max_speed = jockey.horse.speed
        return winner

    def add_horse(self, horse_type: str, horse_name: str,
                  horse_speed: int):
        if horse_type not in self.VALID_BREEDS:
            return

        if self.find_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = self.VALID_BREEDS[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:
        if self.find_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str:
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str) -> str:
        jockey = self.find_jockey_by_name(jockey_name)
        horse = self.find_last_horse_of_type(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if horse and jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str) -> str:
        horse_race = self.find_race_by_type(race_type)
        jockey = self.find_jockey_by_name(jockey_name)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(
                f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return (f"Jockey {jockey_name} has been already "
                    f"added to the {race_type} race.")

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str) -> str:
        horse_race = self.find_race_by_type(race_type)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two "
                            f"participants!")

        winner = self.find_winner(horse_race.jockeys)
        return (f"The winner of the {race_type} race, with a speed of "
                f"{winner.horse.speed}km/h is {winner.name}! "
                f"Winner's horse: {winner.horse.name}.")
