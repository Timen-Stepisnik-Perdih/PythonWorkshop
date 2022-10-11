from abc import ABC, abstractmethod
from pokeballType_abstr import PokeballTypeAbstr
from pokeball_abstr import PokeballAbstr

class ShopAbstr:
    @abstractmethod
    def buyPokeball(self, type: PokeballTypeAbstr):
        pass
    @abstractmethod
    def sellPokemon(self, pokeball: PokeballAbstr):
        pass