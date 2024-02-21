class Zoo:
    __animals = 0

    def __init__(self, name: str, mammals: list = [], fishes: list = [],
                 birds: list = []) -> None:
        self.name = name
        self.mammals = mammals
        self.fishes = fishes
        self.birds = birds

    def add_animals(self, species: str, name: str) -> None:
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        else:
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species: str) -> str:
        if species == "mammal":
            to_unpack = self.mammals
        elif species == "fish":
            to_unpack = self.fishes
            species = "fishe"
        else:
            to_unpack = self.birds
        
        species = f"{species.capitalize()}s"
        result = ", ".join(to_unpack)
        return (f"{species} in {self.name}: {result}\n"
                f"Total animals: {Zoo.__animals}")


zoo_name = input()
animals_count = int(input())
zoo = Zoo(zoo_name)
for _ in range(animals_count):
    animal, name = input().split()
    zoo.add_animals(animal, name)
info_of_type = input()
print(zoo.get_info(info_of_type))
