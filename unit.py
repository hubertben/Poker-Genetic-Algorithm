import numpy
from deck import Deck
from card import Card
import random

class Unit:

    fitness = 0
    weights = []
    value = 0
    ID = 0
    cards = []

    eval_values = [
    'Two High', 
    'Three High', 
    'Four High', 
    'Five High', 
    'Six High',
    'Seven High', 
    'Eight High',
    'Nine High', 
    'Ten High',
    'Jack High', 
    'Queen High',
    'King High', 
    'Ace High',
    'Pair', 
    '2 Pair',
    'Three of a Kind', 
    'Straight',
    'Flush', 
    'Full House',
    'Four of a Kind', 
    'Straight Flush',
    'Royal Flush'
    ]

    def __init__(self, ID, weights_size):
        self.value = 0 
        self.ID = ID
        self.weights = numpy.random.uniform(low = -1, high = 1, size = weights_size)

    def set_cards(self, l):
        self.cards = l

    def print_cards(self):
        print("Player ID: ", self.ID)
        self.cards[0].print_short() 
        self.cards[1].print_short()
        print()

    def get_eval_val(self):
        return self.eval_values[self.value - 1]
