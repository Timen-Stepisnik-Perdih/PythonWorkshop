from implementations.pokemon import Pokemon
from implementations.pokeball import Pokeball
from implementations.trainer import Trainer
from implementations.location import Location, WaterLocation, FireLocation, GrassLocation
import implementations.location

squirtle = Pokemon("squirtle", 100, 100, "water")
charmender = Pokemon("charmender", 100, 100, "fire")

timen = Trainer("Timen")
timen.add_pokeball(Pokeball())
timen.add_pokeball(Pokeball())
timen.add_pokeball(Pokeball())

water_location = WaterLocation()
fire_location = FireLocation()
grass_location = GrassLocation()

location = Location("fire")

breakpoint()
