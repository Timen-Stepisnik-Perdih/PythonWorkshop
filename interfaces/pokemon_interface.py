from abc import ABC, abstractmethod

class PokemonInterface(ABC):
    # @property
    # def name(self):
    #     pass

    # @property
    # @abstractmethod
    # def hp(self):
    #     pass

    # @property
    # @abstractmethod
    # def max_hp(self):
    #     pass

    # @property
    # @abstractmethod
    # def type(self):
    #     pass

    # @property
    # @abstractmethod
    # def strength(self):
    #     pass


    name: str
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
