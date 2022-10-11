from abc import ABC, abstractmethod
import random

from pokemon_abstr import PokemonAbstr
from pokeballType_abstr import PokeballTypeAbstr

class PokeballAbstr:
    pokemon_inside: PokemonAbstr
    type: PokeballTypeAbstr
    
    @abstractmethod
    def __init__(self, type: PokeballTypeAbstr):
        pass
    @abstractmethod
    def attempt_catch(self, pokemon: PokemonAbstr) -> bool:
        pass
    @abstractmethod
    def is_empty(self) -> bool:
        pass   
    @abstractmethod
    def add_pokemon(self, pokemon):
        pass
    @abstractmethod
    def summon_pokemon(self) -> PokemonAbstr:
        pass
    @abstractmethod
    def empty(self):
        pass
    @abstractmethod
    def __str__(self):
        pass