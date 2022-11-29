from abc import ABC, abstractmethod

class PokemonInterface(ABC):
    hp: int
    max_hp: int
    type: str
    @abstractmethod
    def feed(self, food_quantity: int):
        pass

    @abstractmethod
    def __str__(self, food_quantity: int):
        pass

    @abstractmethod
    def battle(self, opponent: 'PokemonInterface'):
        pass
