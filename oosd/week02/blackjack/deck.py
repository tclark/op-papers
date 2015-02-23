import card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in "CDHS":
            for val in range(1, 11):
                self.cards.append(card.Card(val, suit))
            for val in "AKQJ":
                self.cards.append(card.Card(val, suit))
        random.shuffle(self.cards)
        

    def next(self):
        return self.cards.pop()
        



