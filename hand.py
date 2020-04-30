import numpy
from deck import Deck
from card import Card
import random


class Hand:
    def __init__(self, deck):
        self.cards = deck.deal_cards(5)
        self.deck = deck

    def print_cards(self):               
        for c in self.cards:
            c.print_short()
        print()    