import card
import random

class Deck:
    def __init__(self, shufflemethod):
        self.cards = []
        for suit in "CDHS":
            for val in range(2, 11):
                self.cards.append(card.Card(val, suit))
            for val in "AKQJ":
                self.cards.append(card.Card(val, suit))
            self.shuffle = shufflemethod
        

    def next(self):
        return self.cards.pop()
       
def swap(things, p0, p1):
    temp = things[p0]
    things[p0] = things[p1]
    things[p1] = temp

def built_in_shuffle(d):
    random.shuffle(d.cards)

def manual_shuffle(d):
    for pos in xrange(52):
        swap_pos = random.randrange(52)
        swap(d.cards, pos, swap_pos)

def odd_even_shuffle(d):
    for pos in xrange(0,52,2):
        swap_pos = random.randrange(1,52,2)
        swap(d.cards, pos, swap_pos)

def random_swap_shuffle(d):
    for _ in xrange(52):
        swap(d.cards, random.randrange(52), random.randrange(52))

