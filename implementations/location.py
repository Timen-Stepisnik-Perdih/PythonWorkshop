import sys
import os
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../interfaces"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "."))

from pokemon_interface import PokemonInterface
from location_interface import LocationInterface

from pokemon import Pokemon

class Location(LocationInterface):
    def find_pokemon(self) -> PokemonInterface:
        random_float = random.random()
        if random_float < self.probability:
            return random.choice(self.native_pokemons)
        else:
            print("Found nothing")

class WaterLocation(Location):
    type = 'water'
    probability = 0.8
    native_pokemons = [
        Pokemon('Squirle', 120, 120, type),
        Pokemon('Magikarp', 30, 30, type),
        Pokemon('Staryu', 90, 90, type)      
    ]
    
class FireLocation(Location):
    type = 'fire'
    probability = 0.3
    native_pokemons = [
        Pokemon('Magmar', 120, 120, type),
        Pokemon('Ponyta', 30, 30, type),
        Pokemon('Charmender', 90, 90, type)      
    ]
    
class GrassLocation(Location):
    type = 'grass'
    probability = 0.6
    native_pokemons = [
        Pokemon('Bulbasaur', 120, 120, type),
        Pokemon('Oddish', 30, 30, type),
        Pokemon('Gloom', 90, 90, type)      
    ]


# class Location(LocationInterface):

#     type_dictionary = {
#         "water": [Pokemon("Squirtle", 100, 100, "water"), Pokemon("Horsea", 70, 80, "water"),  Pokemon("Magikarp", 1, 10, "water")],
#         "fire": [ Pokemon("Charmender", 100, 100, "fire"), 
                # Pokemon("Ponyta", 100, 100, "fire"), 
                # Pokemon("Vulpix", 60, 90, "fire")]
#     }
#     native_pokemons = [
#         Pokemon("squirtle", 100, 100, "water"),
#         Pokemon("charmender", 100, 100, "fire")
#     ]

#     def __init__(self, name: str, type: str):
#         self.name = name
#         self.type = type

#     def find_pokemon(self) -> PokemonInterface:
#         random_float = random.random()
#         if random_float < 0.3:
#             return random.choice(self.type_dictionary[self.type])
#         else:
#             print("Found nothing")