

from card import Card
import random
class Deck:
    cards = []
    suite = ["Spades", "Diamonds", "Clubs", "Hearts"]
    value = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    ss = ["♠","♦","♣","♥"]
    sv = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]


    def __init__(self):
        for i in range(52):
            self.cards = [Card(i, self.value[(int)(i%13)], self.suite[(int)(i/13)], self.sv[(int)(i%13)], self.ss[(int)(i/13)]) for i in range(52)]
        self.shuffle(1000)

    def print_cards_longHand(self):
        for i in range(52):
            print(self.cards[i].value," of ",self.cards[i].suite)

    def print_cards_shortHand(self):
        for i in range(52):
            print(self.cards[i].ss + "" + self.cards[i].sv)

    def print_card(self, index, l):
        if(l):
            print(self.cards[index].value," of ",self.cards[index].suite)
        else:
            print(self.cards[index].ss + "" + self.cards[index].sv)

    def shuffle(self, i):
        for _ in range(i):  
            index = random.randint(0, len(self.cards) - 1)
            spot = self.cards[index]
            self.cards.pop(index)
            self.cards.append(spot)

    def deal_cards(self, i):
        return_list = []
        for _ in range(i):
            return_list.append(self.cards.pop())
        return return_list

    def give_cards_to_unit(self):
        return_list = []
        for o in range(2):
            return_list.append(self.cards[o])
        return return_list
