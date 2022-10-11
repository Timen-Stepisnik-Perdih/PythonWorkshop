import sys
import random
sys.path.insert(0, 'C:/Users/TimenStepisnikPerdih/Desktop/PythonWorkshop/PythonWorkshop/abstracts')
from pokemon_abstr import PokemonAbstr
from location_abstr import LocationAbstr
from trainer_abstr import TrainerAbstr
from pokemon import Pokemon

class Location(LocationAbstr):
    def battle_and_catch(self, trainer: TrainerAbstr, attackingPokemon: PokemonAbstr) -> bool:
        pokeball = trainer.ready_pokeball()
        if pokeball is None:
            print("Trainer has no ready pokeballs")
            return False
        defendingPokemon = random.choice(self.pokemonArray)
        print("Found pokemon:")
        print(defendingPokemon)
        result = attackingPokemon.battle(defendingPokemon)
        if result:
            pokeball.add_pokemon(defendingPokemon)
            return True
        return False

class WaterLocation(Location):
    type = 'water'
    pokemonArray = [
        Pokemon('Squirle', type, 120),
        Pokemon('Magikarp', type, 30),
        Pokemon('Staryu', type, 90)      
    ]
    
class FireLocation(Location):
    type = 'fire'
    pokemonArray = [
        Pokemon('Magmar', type, 120),
        Pokemon('Ponyta', type, 30),
        Pokemon('Charmender', type, 90)      
    ]
    
class GrassLocation(Location):
    type = 'grass'
    pokemonArray = [
        Pokemon('Bulbasaur', type, 120),
        Pokemon('Oddish', type, 30),
        Pokemon('Gloom', type, 90)      
    ]
