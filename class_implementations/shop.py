import sys
from abstracts.pokeballType_abstr import PokeballTypeAbstr
sys.path.insert(0, 'C:/Users/TimenStepisnikPerdih/Desktop/PythonWorkshop/PythonWorkshop/abstracts')
from shop_abstr import ShopAbstr
from pokeballType_abstr import PokeballTypeAbstr
from trainer_abstr import TrainerAbstr
from pokeball_abstr import PokeballAbstr
from pokeball import Pokeball

class Shop(ShopAbstr):
    pokemon_cost = 20
    
    def buyPokeball(self, type: PokeballTypeAbstr, trainer: TrainerAbstr) -> bool:
        if trainer.money < type.cost:
            return False
        trainer.money -= type.cost
        trainer.pokeballs.append(Pokeball(type))
        return True
    
    def sellPokemon(self, pokeball: PokeballAbstr, trainer: TrainerAbstr) -> bool:
        if pokeball.is_empty():
            return False
        trainer.money += self.pokemon_cost
        pokeball.empty()
        return True