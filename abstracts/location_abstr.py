from abc import ABC, abstractmethod
from typing import List

from pokemon_abstr import PokemonAbstr

class LocationAbstr:
    pokemonArray: List[PokemonAbstr]
    
    @abstractmethod
    def battle_and_catch(self, pokemon: PokemonAbstr):
        pass