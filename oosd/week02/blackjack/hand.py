import deck

class Hand:

    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def size(self):
        return len(self.cards)

    def score(self):
        # sperate cards into aces and others
        regular_cards = [c for c in self.cards if c.value != "A"]
        aces = [c for c in self.cards if c.value == "A"]

        #tally up regular card values
        points = 0
        for c in regular_cards:
            if isinstance(c.value, basestring):
                points += 10
            else:
                points += c.value
        # now add in aces
        for c in aces:
            if points + 11 <= 21:
                points += 11
            else:
                points += 1

        return points


    def __repr__(self):
        hand_string = ""
        for card in self.cards:
            hand_string += str(card)
            hand_string += " "
        return hand_string
