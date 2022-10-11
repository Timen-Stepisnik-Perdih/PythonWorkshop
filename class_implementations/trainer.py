import sys
import random
from tracemalloc import start
sys.path.insert(0, 'C:/Users/TimenStepisnikPerdih/Desktop/PythonWorkshop/PythonWorkshop/abstracts')
from pokemon_abstr import PokemonAbstr
from trainer_abstr import TrainerAbstr
from pokeball_abstr import PokeballAbstr
from pokeballType import BasePokeball
from pokeball import Pokeball
from pokemon import Pokemon

class Trainer(TrainerAbstr):
    starter_pokemons = [
            Pokemon('bulbasaur', 'grass', 120),
            Pokemon('charmander', 'fire', 110),
            Pokemon('squirtle', 'water', 115)
    ]
    
    def __init__(self, name: str):
        self.name = name
        self.money = 30
        self.pokeballs = [Pokeball(BasePokeball())]
        
        starter_pokemon = random.choice(self.starter_pokemons)
        self.pokeballs[0].add_pokemon(starter_pokemon)
        
    def summon_pokemon(self, targetName: str) -> PokemonAbstr:
        for pokeball in self.pokeballs:
            if pokeball.pokemon_inside.name == targetName:
                return pokeball.summon_pokemon()
        return None
    
    def ready_pokeball(self) -> PokeballAbstr:
        for pokeball in self.pokeballs:
            if pokeball.is_empty():
                return pokeball
        return None
    
    def __str__(self):
        return_string = ""
        return_string += "Name: " + self.name + "\n"
        return_string += "Money available: " + self.money + "\n"
        return_string += "Pokeballs:\n"
        for pokeball in self.pokeballs:
            return_string += pokeball.__str__() + "\n"
        return return_string