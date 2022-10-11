from abc import ABC, abstractmethod
import random

from pokemon_abstr import PokemonAbstr
from pokeball_abstr import PokeballAbstr

class PokeballAbstr:
    pokemon_inside: PokemonAbstr
    type: PokeballAbstr
    
    @abstractmethod
    def attempt_catch(self, pokemon: PokemonAbstr) -> bool:
        pass
    @abstractmethod
    def is_empty(self) -> bool:
        pass    
    @abstractmethod
    def summon_pokemon(self) -> PokemonAbstr:
        pass