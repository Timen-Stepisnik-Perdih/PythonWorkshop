import sys
import os
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../interfaces"))
from pokemon_interface import PokemonInterface

class Pokemon(PokemonInterface):
    possible_damages = [10, 20, 30, 50]

    def __init__(self, name: str, hp: int, max_hp: int, primary_type: str):
        self.name = name
        self.type = primary_type  # water, fire, grass
        self.max_hp = max_hp
        self.hp = max_hp

    @staticmethod
    def typewheel(type1, type2):
        result_map = {0 : "lose", 1 : "win", -1 : "tie"}
        # The mapping between moves and numbers
        game_map = {"water": 0, "fire": 1, "grass": 2}
        # Win-lose matrix
        rps_table = [
            [-1, 1, 0],  # water
            [0, -1, 1],  # fire
            [1, 0, -1]   # grass
        ]
        result = rps_table[game_map[type1]][game_map[type2]]
        return result_map[result]
    
    def feed(self, quantity):
        self.hp += quantity
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def battle(self, other): # fire 80 - hp     # water 60 - hp
        result = self.typewheel(self.type, other.type)

        if result == "tie":
            self.hp -= random.choice(self.possible_damages)
            other.hp -= random.choice(self.possible_damages)
        elif result == "win":
            self.hp -= random.choice(self.possible_damages) / 2
            other.hp -= random.choice(self.possible_damages) * 2
        elif result == "lose":
            self.hp -= random.choice(self.possible_damages) * 2
            other.hp -= random.choice(self.possible_damages) / 2

        if self.hp <= 0:
            self.hp = 0
            print(self.name + " is defeated!")

        if other.hp <= 0:
            other.hp = 0
            print(other.name + " is defeated!")

        # result = self.typewheel(self.type, other.type)
        # if result == 'lose':
        #     self.hp = 0
        #     print(f"{self.name} fainted!")
        # elif result == 'tie':
        #     self.hp -= 10
        #     other.hp -= 10
        #     print(f"{self.name} and {other.name} battled hard. It's a tie.")
        # elif result == 'win':
        #     other.hp = 0
        #     print(f"{self.name} won. Congratulations!")

    def __str__(self):
        return f"{self.name} ({self.type}): {self.hp}/{self.max_hp}"
