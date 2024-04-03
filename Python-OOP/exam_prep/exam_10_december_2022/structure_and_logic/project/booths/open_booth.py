from project.booths.booth import Booth


class OpenBooth(Booth):

    def reserve(self, number_of_people: int) -> None:
        price = number_of_people * 2.50
        self.price_for_reservation = price
        self.is_reserved = True
