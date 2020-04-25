'''

Poker Genetic Algorithm

Python Scripts Developed by
Ben Hubert

Current Verions does not support genetic learning
Only basic displays

'''

import numpy
from deck import Deck
from generation import Generation
from population import Population
import random

d = Deck()
p = Population(10, 3)
gen = Generation(p)
gen.hand.print_cards()
gen.assign_unit_value()
gen.print_stats()