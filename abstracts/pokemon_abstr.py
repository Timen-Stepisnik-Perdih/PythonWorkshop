from abc import ABC, abstractmethod

class PokemonAbstr:
    name: str
    primary_type: str
    max_hp: int
    hp: int
    
    @abstractmethod
    def __init__(self, name: str, primary_type: str, max_hp: int):
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