from abc import ABC, abstractmethod, abstractproperty
from pokemon_interface import PokemonInterface 
from pokeball_interface import PokeballInterface

class TrainerInterface(ABC):
    pokeballs: list[PokeballInterface]
    name: str
    experience: int

    @abstractmethod
    def summon_pokemon(self, pokemon_name: str) -> PokemonInterface:
        pass    

    @abstractmethod
    def add_pokeball(self, pokeball: PokeballInterface):
        pass

    @abstractmethod
    def throw_empty_pokeball(self, target_pokemon: PokemonInterface):
        pass


