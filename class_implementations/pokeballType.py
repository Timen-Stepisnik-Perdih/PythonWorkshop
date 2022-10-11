import sys
sys.path.insert(0, 'C:/Users/TimenStepisnikPerdih/Desktop/PythonWorkshop/PythonWorkshop/abstracts')
from pokeballType_abstr import PokeballTypeAbstr

class BasePokeball(PokeballTypeAbstr):
    cost = 1
    catch_probability = 0.5
    
class AdvancedPokeball(PokeballTypeAbstr):
    cost = 4
    catch_probability = 0.7
    
class MasterPokeball(PokeballTypeAbstr):
    cost = 10
    catch_probability = 0.9