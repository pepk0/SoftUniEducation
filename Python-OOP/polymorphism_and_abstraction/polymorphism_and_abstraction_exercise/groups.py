class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}",
                     self.people + other.people)

    def __repr__(self) -> str:
        people = ", ".join(str(person) for person in self.people)
        return f"Group {self.name} with members {people}"

    # THIS IS REDUNDANT IF WE HAVE A GETITEM METHOD OVERWRITTEN
    # def __iter__(self) -> str:
    #     for index, individual in enumerate(self.people):
    #         yield f"Person {index}: {individual}"

    def __getitem__(self, index) -> str:
        return f"Person {index}: {self.people[index]}"
