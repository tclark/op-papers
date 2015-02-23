class Card:
    suits = frozenset("CDHS")
    values = frozenset(range(1, 11) + list("KQJA"))

    def __init__(self, value, suit):
        if(suit in self.suits and value in self.values):
            self.value = value
            self.suit = suit
        else:
            raise ValueError("Illegal suit or value supplied to Card constructor")

    def __repr__(self):
        return str(self.value) + self.suit


