from abc import ABC, abstractmethod
from pokemon_interface import PokemonInterface

class LocationInterface(ABC):
    name: str
    type: str
    native_pokemons: list[PokemonInterface]

    @abstractmethod
    def find_pokemon(self):
        pass