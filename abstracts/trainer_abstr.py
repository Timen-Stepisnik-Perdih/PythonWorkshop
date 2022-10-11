from abc import ABC, abstractmethod
from typing import List
from pokemon_abstr import PokemonAbstr
from pokeball_abstr import PokeballAbstr

class TrainerAbstr:
    pokeballs: List[PokeballAbstr]
    money: int

    @abstractmethod
    def summon_pokemon(self, targetName: str) -> PokemonAbstr:
        pass
        # for pokeball in self.pokeballs:
        #     if pokeball.pokemon_inside.name == targetName:
        #         return pokeball.summon_pokemon()
        # return None