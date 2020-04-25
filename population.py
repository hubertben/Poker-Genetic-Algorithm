import numpy
from deck import Deck
from card import Card
from unit import Unit
from hand import Hand
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