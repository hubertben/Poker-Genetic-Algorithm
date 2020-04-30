
import numpy
from generation import Generation
from deck import Deck
from population import Population
from step import Step
import random

class Driver:


    def __init__(self, pop_size, weight_size, gen_loop_count, batch_size):
        self.p = Population(pop_size, weight_size, 0)
        self.ran = gen_loop_count
        self.step = batch_size

    def run(self):
        max_unit = 0
        for i in range(self.ran):
            print("Generation ", i)
            gen = Generation(self.p)
            #gen.hand.print_cards()
            gen.assign_unit_value(0)
            #gen.print_stats()
            gen.calc_fitness(self.step, 0)

            #for i in range(p.size):
            #    print(gen.population.units[i].fitness)

            if(i == self.ran - 1):
                break


            max_val = 0          
            for i in range(gen.population.size):    
                if(gen.population.units[i].fitness > max_val):
                    max_unit = gen.population.units[i]
                    max_val = gen.population.units[i].fitness

            print(max_unit.fitness)
            s = Step(gen)
            gen.population.units = s.generate_mating_pool()

        max_val = 0
        max_unit = 0
        for i in range(gen.population.size):    
            if(gen.population.units[i].fitness > max_val):
                max_unit = gen.population.units[i]
                max_val = gen.population.units[i].fitness

        print(max_unit.weights)
        return max_unit.weights