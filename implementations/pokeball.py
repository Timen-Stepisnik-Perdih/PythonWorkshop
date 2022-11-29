import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../interfaces"))

from pokeball_interface import PokeballInterface
from pokemon_interface import PokemonInterface

class Pokeball(PokeballInterface):
    pokemon: PokemonInterface = None

    def catch_pokemon(self, caught_pokemon: PokemonInterface):
        self.pokemon = caught_pokemon

    def get_pokemon(self) -> PokemonInterface:
        return self.pokemon

    def is_empty(self) -> bool:
        return self.pokemon == None

    def get_pokemon_name(self):
        return self.pokemon.name