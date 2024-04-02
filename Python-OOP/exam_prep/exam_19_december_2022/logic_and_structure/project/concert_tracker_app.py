from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer,
                            "Singer": Singer}

    def __init__(self) -> None:
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @staticmethod
    def get_musician_by_name_from(musician_name: str, collection):
        try:
            return [m for m in collection if m.name == musician_name][0]
        except IndexError:
            return None

    def get_band_by_name(self, band_name: str):
        try:
            return [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            return None

    def get_concert_by_place(self, place: str):
        try:
            return [c for c in self.concerts if c.place == place][0]
        except IndexError:
            return None

    @staticmethod
    def play_music(band: Band, drummer: str, singer: str,
                   guitarist: str) -> bool:
        drummer_skills = [s for m in band.members if
                          m.__class__.__name__ == "Drummer" for s in m.skills]
        singer_skills = [s for m in band.members if
                         m.__class__.__name__ == "Singer" for s in m.skills]
        guitarist_skills = [s for m in band.members if
                            m.__class__.__name__ == "Guitarist" for s in
                            m.skills]

        valid_drummer = drummer in drummer_skills
        valid_singer = singer in singer_skills
        valid_guitarist = guitarist in guitarist_skills

        return valid_drummer and valid_singer and valid_guitarist

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if self.get_musician_by_name_from(name, self.musicians):
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        if self.get_band_by_name(name):
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float,
                       expenses: float, place: str) -> str:
        concerts = self.get_concert_by_place(place)
        if concerts:
            raise Exception(
                f"{place} is already registered for {concerts.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:

        musician = self.get_musician_by_name_from(musician_name,
                                                  self.musicians)
        band = self.get_band_by_name(band_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str,
                                  band_name: str) -> str:
        band = self.get_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.get_musician_by_name_from(musician_name, band.members)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str:
        band = self.get_band_by_name(band_name)
        concerts = self.get_concert_by_place(concert_place)

        for band_member in self.VALID_MUSICIAN_TYPES:
            if band_member not in band.get_musician_types():
                raise ValueError(f"{band_name} can't start the concert"
                                 f" because it doesn't have enough members!")

        # TODO Implement logic for checks

        profit = concerts.audience * concerts.ticket_price - concerts.expenses
        return (f"{band.name} gained {profit:.2f}$ from the"
                f" {concerts.genre} concert in {concerts.place}.")
