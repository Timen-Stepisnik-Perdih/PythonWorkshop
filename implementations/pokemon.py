import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../interfaces"))

## C:/Timen/..../projekt/implementations/../interfaces
from pokemon_interface import PokemonInterface

class Pokemon(PokemonInterface):
    name: str
    hp: int
    max_hp: int
    type: str

    @staticmethod
    def typewheel(my_type:str, opponent_type:str) -> str:
        result_map = {0 : "tie", 1 : "win", -1 : "lose"}
        # The mapping between moves and numbers
        game_map = {"water": 0, "fire": 1, "grass": 2}
        # Win-lose matrix
        rps_table = [
            [0, 1, -1],  # water
            [-1, 0, 1],  # fire
            [1, -1, 0]   # grass
        ]
        result = rps_table[game_map[my_type]][game_map[opponent_type]]
        return result_map[result]

    def __init__(self, name: str, hp: int, max_hp: int, type: str):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.type = type

    def __str__(self):
        return self.name + ": " + self.type + " " + str(self.hp)+"/"+str(self.max_hp)

    def feed(self, food_quantity: int):
        self.hp += food_quantity
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def battle(self, opponent: 'Pokemon') -> bool:
        result = self.typewheel(self.type, opponent.type)
        if result == 'lose':
            self.hp = 0
            print(f"{self.name} fainted!")
            return False
        elif result == 'tie':
            self.hp -= 10
            opponent.hp -= 10
            print(f"{self.name} and {opponent.name} battled hard. It's a tie.")
            return False
        elif result == 'win':
            opponent.hp = 0
            print(f"{self.name} won. Congratulations!")
            print(f"{opponent.name} caught!")
            return True


