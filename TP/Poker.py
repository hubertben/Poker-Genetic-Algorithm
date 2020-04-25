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


class Hand:
    def __init__(self, deck):
        self.cards = deck.deal_cards(5)
        self.deck = deck

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
            print(self.population.units[i].get_eval_val(), end='  ')
            self.population.units[i].print_cards()
            print()
            

    def straight_check(self, l):
        new_list = sorted(l, key=lambda card: card.abs_val)
        count = 0
        for i in range(6):
            if((new_list[i].abs_val + 1) == new_list[i+1].abs_val):
                count += 1
            else:
                count = 0   
            if(count == 4):
                return True
        return False
    
    def flush_check(self, l):
        suites = [0,0,0,0]
        for i in range(7):
            if(l[i].suite == 'Spades'):
                suites[0] += 1
            if(l[i].suite == 'Diamonds'):
                suites[1] += 1
            if(l[i].suite == 'Clubs'):
                suites[2] += 1
            if(l[i].suite == 'Hearts'):
                suites[3] += 1
        
        for i in range(4):
            if(suites[i] >= 5):
             return True
        return False        


    def match_check(self, l):
        used_cards = []
        used_cards_count = [0,0,0,0,0,0,0]
        for i in range(7):
            if(l[i].abs_val in used_cards):   
                used_cards_count[used_cards.index(l[i].abs_val)] += 1
            else:
                used_cards.append(l[i].abs_val)

        if(3 in used_cards_count):
            return 20
        if(2 in used_cards_count and 1 in used_cards_count):
            return 19
        if(2 in used_cards_count):
            return 16
        
        for i in range(7):
            if(used_cards_count[i] == 1):
                for j in range(i+1, 7):
                    if(used_cards_count[j] == 1):
                        return 15

        if(1 in used_cards_count):
            return 14
        return 0

    def high_card_check(self, l):
        new_list = sorted(l, key=lambda card: card.abs_val)
        return new_list[6].abs_val
        

    '''
        22 : Royal Flush
        21 : Straight Flush
        20 : Four of a Kind
        19 : Full House
        18 : Flush
        17 : Straight
        16 : Three of a Kind
        15 : Two Pair
        14 : Pair
        13 : Ace High
        12 : King High
        .
        .
        .
        2 : Three High
        1 : Two High
    '''
    def calc_hand(self, index):
        
        comp_list = self.hand.cards + (self.population.units[index].cards)
            
        if(self.straight_check(comp_list)):
            if(self.flush_check(comp_list)):
                if(self.high_card_check(comp_list) == 14):
                    return 22
                else:
                    return 21
            else:
                return 17

        if(self.flush_check(comp_list)):
            return 18

        if(self.match_check(comp_list) != 0):
            return self.match_check(comp_list)

        return self.high_card_check(comp_list) - 1       
            
    def assign_unit_value(self):
        for index in range(self.population.size):
            self.population.units[index].value = self.calc_hand(index)

d = Deck()
p = Population(10, 3)
gen = Generation(p)
gen.hand.print_cards()
gen.assign_unit_value()
gen.print_stats()

