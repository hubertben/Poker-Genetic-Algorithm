'''

Poker Genetic Algorithm

Python Scripts Developed by
Ben Hubert

Current Verions does not support genetic learning
Only basic displays

'''

import numpy
from deck import Deck
from card import Card
import random

class Population:

    units = []
    size = 0

    def __init__(self, size, weights_size):
        self.size = size
        self.units = [Unit(i, weights_size) for i in range(size)]
    
    def print_units_weights(self):
        for i in range(self.size):
            print(self.units[i].weights)

class Unit:

    fitness = 0
    weights =[]
    value = 0
    ID = 0
    cards = []

    def __init__(self, ID, weights_size):
        self.value = 500 
        self.ID = ID
        self.weights = numpy.random.uniform(low = -1, high = 1, size = weights_size)

    def set_cards(self, l):
        self.cards = l

    def print_cards(self):
        print("Player ID: ", self.ID)
        self.cards[0].print_short() 
        self.cards[1].print_short()
        print()

class Hand:
    def __init__(self, deck):
        self.cards = deck.deal_cards(5)

    def print_cards(self):               
        for c in self.cards:
            c.print_short()
        print()    

class Generation:
    def __init__(self, population):
        self.population = population
        self.deck = Deck()
        self.games = []
        self.hand = Hand(self.deck)
        
        for p in range(self.population.size):
            self.deck.shuffle(1000)
            population.units[p].set_cards(self.deck.give_cards_to_unit())
            

    def print_stats(self):
        for i in range(self.population.size):
            self.population.units[i].print_cards()
        
    def calc_hand(self):
        return




d = Deck()
p = Population(5, 3)

gen = Generation(p)

gen.hand.print_cards()
gen.print_stats()



