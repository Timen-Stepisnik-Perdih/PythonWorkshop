import sys
sys.path.insert(0, 'C:/Users/TimenStepisnikPerdih/Desktop/PythonWorkshop/PythonWorkshop/class_implementations')

from location import Location, WaterLocation, GrassLocation, FireLocation
from trainer import Trainer
from pokemon import Pokemon
from shop import Shop
from pokeball import Pokeball
from pokeballType import BasePokeball, MasterPokeball, AdvancedPokeball


timen = Trainer("Timen")
shop = Shop()
water_loc = WaterLocation()
grass_loc = GrassLocation()
fire_loc = FireLocation()

print(timen)
breakpoint()