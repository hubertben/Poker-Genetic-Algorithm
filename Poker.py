'''

Poker Genetic Algorithm

Python Scripts Developed by
Ben Hubert

Current Verions does not support genetic learning
Only basic displays

'''

from driver import Driver
from generation import Generation
from population import Population
from deck import Deck
from step import Step

w = []

'''
d = Driver(50, 100, 10, 5)
w = d.run()
'''

money = 1000

p = Population(1, len(w), 0)
g = Generation(p)

while True:
    g.assign_unit_value(0)
    g.hand.print_cards()

    my_cards = g.deck.deal_cards(2)

    my_cards[0].print_short()
    my_cards[1].print_short()

    print("\nHow much Money would you like to bet?")
    print("You Have", money, "Dollars")
    bet = int(input())

    eval = g.calc_hand(0, my_cards)

    print("\n")

    g.print_stats()
    t = g.calc_fitness(1, eval)
    
    if(t):
        money += bet*2
    else:
        money -= bet
    
    print("Human Evaluation:", eval, "Unit Evaluation:", g.population.units[0].value)

    print(g.population.units[0].fitness)

    g.deck.cards.append(my_cards[0])
    g.deck.cards.append(my_cards[1])

    g = Generation(p)



