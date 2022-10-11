from abc import ABC, abstractmethod
from typing import List
from pokemon_abstr import PokemonAbstr
from pokeball_abstr import PokeballAbstr

class TrainerAbstr:
    pokeballs: List[PokeballAbstr]
    money: int
    name: str
    
    @abstractmethod
    def __init__(self, name: str):
        pass

    @abstractmethod
    def summon_pokemon(self, targetName: str) -> PokemonAbstr:
        pass
    
    @abstractmethod
    def ready_pokeball(self) -> PokeballAbstr:
        pass