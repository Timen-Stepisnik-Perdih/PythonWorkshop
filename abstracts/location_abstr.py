from abc import ABC, abstractmethod
from typing import List

from pokemon_abstr import PokemonAbstr

class LocationAbstr:
    pokemonArray: List[PokemonAbstr]
    type: str
    
    @abstractmethod
    def battle_and_catch(self, attackingPokemon: PokemonAbstr) -> PokemonAbstr:
        pass