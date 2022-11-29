from implementations.pokemon import Pokemon
from implementations.pokeball import Pokeball
from implementations.trainer import Trainer


squirtle = Pokemon("squirtle", 100, 100, "water")
charmender = Pokemon("charmender", 100, 100, "fire")

timen = Trainer("Timen")
timen.add_pokeball(Pokeball())
timen.add_pokeball(Pokeball())
timen.add_pokeball(Pokeball())


breakpoint()
