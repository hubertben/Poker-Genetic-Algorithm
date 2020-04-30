
from generation import Generation
from population import Population
from random import randint
from unit import Unit

'''
Evaluations with a score of 
<1 : Fold
1 : Call
>1 : Bet by a sigmoid of the number beween (0,1]
'''

class Step:

    def __init__(self, gen):
        self.gen = gen
        self.pop = gen.population

    def merge_genes(self, a, b):
        new_weights = []
        
        for i in range(self.pop.weights_size):
            n = randint(1, 2)
            if(n == 1): 
                new_weights.append(a.weights[i])
            else: 
                new_weights.append(b.weights[i])

        return new_weights

    def produce_pool(self, pool):

        new_pop = []
        s = self.pop.size

        for _ in range(s):
            parent_a = pool[randint(1, s-1)]
            parent_b = pool[randint(1, s-1)]

            new_unit = Unit(0, len(parent_a.weights), self.merge_genes(parent_a, parent_b))
            new_pop.append(new_unit)

        return new_pop



    def generate_mating_pool(self):
        pool = []
        maxfit = -100000000

        for i in range(self.pop.size):
            if(self.pop.units[i].fitness > maxfit):
                maxfit = self.pop.units[i].fitness
        
        for i in range(self.pop.size):
            self.pop.units[i].fitness /= maxfit

        for i in range(self.pop.size):
            n = self.pop.units[i].fitness * 100
        
            # Bias Add

            for _ in range(int(n)):
                pool.append(self.pop.units[i])

        return self.produce_pool(pool)
    
    






