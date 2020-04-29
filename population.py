import numpy
from deck import Deck
from card import Card
from unit import Unit
from hand import Hand
import random

class Population:

    units = []
    size = 0
    

    def __init__(self, size, weights_size, u):
        self.size = size
        self.weights_size = weights_size
        if(u == 0):
            self.units = [Unit(i, weights_size, 0) for i in range(size)]
        else:
            self.units = u

    def print_units_weights(self):
        for i in range(self.size):
            print(self.units[i].weights)