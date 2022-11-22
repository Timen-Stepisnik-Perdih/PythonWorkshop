import sys
import os
from abstracts.pokeballType_abstr import PokeballTypeAbstr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../abstracts"))
from shop_abstr import ShopAbstr
from pokeballType_abstr import PokeballTypeAbstr
from trainer_abstr import TrainerAbstr
from pokeball_abstr import PokeballAbstr
from pokeball import Pokeball

class Shop(ShopAbstr):
    pokemon_cost = 20
    
    def buy_pokeball(self, type: PokeballTypeAbstr, trainer: TrainerAbstr) -> bool:
        if trainer.money < type.cost:
            return False
        trainer.money -= type.cost
        trainer.pokeballs.append(Pokeball(type))
        return True
    
    def sell_pokemon(self, pokeball: PokeballAbstr, trainer: TrainerAbstr) -> bool:
        if pokeball.is_empty():
            return False
        trainer.money += self.pokemon_cost
        pokeball.empty()
        return True