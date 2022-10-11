from abc import ABC, abstractmethod
from pokeballType_abstr import PokeballTypeAbstr
from pokeball_abstr import PokeballAbstr
from trainer_abstr import TrainerAbstr

class ShopAbstr:
    @abstractmethod
    def buy_pokeball(self, type: PokeballTypeAbstr, trainer: TrainerAbstr) -> bool:
        pass
    @abstractmethod
    def sell_pokemon(self, pokeball: PokeballAbstr, trainer: TrainerAbstr) -> bool:
        pass