import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../interfaces"))

from trainer_interface import TrainerInterface
from pokeball_interface import PokeballInterface
from pokemon_interface import PokemonInterface

class Trainer(TrainerInterface):
    pokeballs: list[PokeballInterface]
    name: str
    experience: int

    def __init__(self, name:str):
        self.name = name
        self.experience = 0
        self.pokeballs = []

    def summon_pokemon(self, pokemon_name: str) -> PokemonInterface:
        for pokeball in self.pokeballs:
            if pokeball.is_empty():
                continue
            if pokeball.get_pokemon_name() == pokemon_name:
                return pokeball.get_pokemon()
        return None # Nimamo tega pokemona

    def add_pokeball(self, pokeball: PokeballInterface):
        self.pokeballs.append(pokeball)

    def throw_empty_pokeball(self, target_pokemon: PokemonInterface):
        for pokeball in self.pokeballs:
            if pokeball.is_empty():
                pokeball.catch_pokemon(target_pokemon)
                return

        print("No empty pokeball")

 