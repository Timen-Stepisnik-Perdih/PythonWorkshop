import sys
import random
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../abstracts"))
from pokeball_abstr import PokeballAbstr
from pokemon_abstr import PokemonAbstr
from pokeballType_abstr import PokeballTypeAbstr

class Pokeball(PokeballAbstr):
    def __init__(self, type: PokeballTypeAbstr):
        self.type = type
        self.pokemon_inside = None
        
    def attempt_catch(self, pokemon: PokemonAbstr) -> bool: 
        if (random.uniform(0, 1) < self.type.catch_probability):
            self.add_pokemon(pokemon)
            return True
        return False
    
    def is_empty(self) -> bool:
        return self.pokemon_inside is None
    
    def add_pokemon(self, pokemon):
        self.pokemon_inside = pokemon
        
    def summon_pokemon(self) -> PokemonAbstr:
        return self.pokemon_inside
    
    def empty(self):
        self.pokemon_inside = None
        
    def __str__(self):
        return_string = ""
        if self.is_empty():
            return_string += "Empty " + self.type.name + " ball \n"
        else:
            return_string += self.pokemon_inside.__str__() + "\n"
        return return_string