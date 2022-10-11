import sys
import random
sys.path.insert(0, 'C:/Users/TimenStepisnikPerdih/Desktop/PythonWorkshop/PythonWorkshop/abstracts')
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
        return self.pokemon_inside is not None
    
    def add_pokemon(self, pokemon):
        self.pokemon_inside = pokemon
        
    def summon_pokemon(self) -> PokemonAbstr:
        return self.pokemon_inside
    
    def empty(self):
        self.pokemon_inside = None