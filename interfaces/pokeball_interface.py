from abc import ABC, abstractmethod
from pokemon_interface import PokemonInterface

class PokeballInterface(ABC):
    pokemon: PokemonInterface

    @abstractmethod
    def catch_pokemon(self, caught_pokemon: PokemonInterface):
        pass

    @abstractmethod
    def get_pokemon(self) -> PokemonInterface:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get_pokemon_name(self) -> str:
        pass