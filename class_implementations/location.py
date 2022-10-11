import sys
import random
sys.path.insert(0, 'C:/Users/TimenStepisnikPerdih/Desktop/PythonWorkshop/PythonWorkshop/abstracts')
from pokemon_abstr import PokemonAbstr
from location_abstr import LocationAbstr
from trainer_abstr import TrainerAbstr

class Location(LocationAbstr):
    def battle_and_catch(self, trainer: TrainerAbstr, attackingPokemon: PokemonAbstr) -> bool:
        pokeball = trainer.ready_pokeball()
        if pokeball is None:
            print("Trainer has no ready pokeballs")
            return False
        defendingPokemon = random.choice(self.pokemonArray)
        result = attackingPokemon.battle(defendingPokemon)
        if result:
            pokeball.add_pokemon(defendingPokemon)
            return True
        return False

class WaterLocation(Location):
    type = 'water'
    pokemonArray = [
        PokemonAbstr('Squirle', type, 120),
        PokemonAbstr('Magikarp', type, 30),
        PokemonAbstr('Staryu', type, 90)      
    ]
    
class FireLocation(Location):
    type = 'fire'
    pokemonArray = [
        PokemonAbstr('Magmar', type, 120),
        PokemonAbstr('Ponyta', type, 30),
        PokemonAbstr('Charmender', type, 90)      
    ]
    
class GrassLocation(Location):
    type = 'grass'
    pokemonArray = [
        PokemonAbstr('Bulbasaur', type, 120),
        PokemonAbstr('Oddish', type, 30),
        PokemonAbstr('Gloom', type, 90)      
    ]
