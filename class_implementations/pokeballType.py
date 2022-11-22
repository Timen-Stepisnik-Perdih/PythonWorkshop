import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../abstracts"))
from pokeballType_abstr import PokeballTypeAbstr

class BasePokeball(PokeballTypeAbstr):
    name = "Base"
    cost = 1
    catch_probability = 0.5
    
class AdvancedPokeball(PokeballTypeAbstr):
    name = "Advanced"
    cost = 4
    catch_probability = 0.7
    
class MasterPokeball(PokeballTypeAbstr):
    name = "Master"
    cost = 10
    catch_probability = 0.9