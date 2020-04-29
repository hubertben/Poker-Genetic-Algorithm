'''

Poker Genetic Algorithm

Python Scripts Developed by
Ben Hubert

Current Verions does not support genetic learning
Only basic displays

'''

import numpy
from generation import Generation
from deck import Deck
from unit import Unit
from population import Population
from step import Step
import random




d = Deck()
p = Population(10, 500, 0)

for i in range(4):
    gen = Generation(p)
    gen.hand.print_cards()

    gen.assign_unit_value(0)
    gen.print_stats()

    gen.calc_fitness(20)

    for i in range(p.size):
        print(gen.population.units[i].fitness)

    s = Step(gen)
    gen.population.units = s.generate_mating_pool()


gen = Generation(p)
gen.hand.print_cards()

gen.assign_unit_value(0)
gen.print_stats()
gen.calc_fitness(20)
for i in range(p.size):
        print(gen.population.units[i].fitness)