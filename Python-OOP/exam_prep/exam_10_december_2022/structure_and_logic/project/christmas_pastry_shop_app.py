from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self) -> None:
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def get_delicacy_by_name(self, delicacy_name: str):
        try:
            return [x for x in self.delicacies if
                    delicacy_name == x.name][0]
        except IndexError:
            return None

    def get_booth_by_number(self, booth_number: int):
        try:
            return [x for x in self.booths if booth_number == x.booth_number][0]
        except IndexError:
            return None

    def get_first_valid_booth(self, space_needed: int):
        for booth in self.booths:
            if booth.capacity >= space_needed and not booth.is_reserved:
                return booth
        return None

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:

        if type_delicacy not in self.VALID_DELICACIES_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if self.get_delicacy_by_name(name):
            raise Exception(f"{name} already exists!")

        delicacy = self.VALID_DELICACIES_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return (f"Added delicacy {delicacy.name} - "
                f"{type_delicacy} to the pastry shop.")

    def add_booth(self, type_booth: str, booth_number: int,
                  capacity: int) -> str:
        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        if self.get_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        booth = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth.booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        booth = self.get_first_valid_booth(number_of_people)

        if not booth:
            raise Exception(
                f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return (f"Booth {booth.booth_number} has been "
                f"reserved for {number_of_people} people.")

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        booth = self.get_booth_by_number(booth_number)
        delicacy = self.get_delicacy_by_name(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number: int) -> str:
        booth = self.get_booth_by_number(booth_number)

        bill = booth.price_for_reservation + sum(
            x.price for x in booth.delicacy_orders)

        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f"Booth {booth.booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."
