from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: list = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        if room_number in self.rooms:
            room = self.rooms[self.rooms.index(room_number)]
            added = room.take_room(people)
            if not added:
                self.guests += people

    def free_room(self, room_number: int):
        if room_number in self.rooms:
            room = self.rooms[self.rooms.index(room_number)]
            self.guests -= room.guests
            room.free_room()

    def status(self) -> str:
        free_rooms = ", ".join(
            str(room) for room in self.rooms if not room.is_taken)
        taken_rooms = ", ".join(
            str(room) for room in self.rooms if room.is_taken)

        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {free_rooms}\nTaken rooms: {taken_rooms}")
