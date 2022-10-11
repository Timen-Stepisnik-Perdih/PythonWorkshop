from abc import ABC, abstractmethod

class PokemonAbstr:
    name: str
    primary_type: str
    max_hp: int
    hp: int
    
    @abstractmethod
    def __init__(self, name, primary_type, max_hp):
        pass
    @abstractmethod
    def feed(self):
        pass
    @abstractmethod
    def battle(self, other):
        pass
    @abstractmethod
    def __str__(self):
        pass