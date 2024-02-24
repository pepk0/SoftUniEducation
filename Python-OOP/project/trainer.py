from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons: list = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        total_pokemons = "\n".join(
            f"- {el.pokemon_details()}" for el in self.pokemons)
        result = (f"Pokemon Trainer {self.name}\nPokemon count "
                  f"{len(self.pokemons)}\n{total_pokemons}")
        return result


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
