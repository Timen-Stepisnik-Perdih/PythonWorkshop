import sys
sys.path.insert(0, 'C:/Users/TimenStepisnikPerdih/Desktop/PythonWorkshop/PythonWorkshop/abstracts')
from pokemon_abstr import PokemonAbstr
from trainer_abstr import TrainerAbstr
from pokeball_abstr import PokeballAbstr

class Trainer(TrainerAbstr):
    def __init__(self, name: str):
        self.name = name
        self.money = 30
        self.pokeballs = []
        
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