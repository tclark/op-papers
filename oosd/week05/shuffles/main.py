import math
import sys
import card
import deck

def initialise_results():
    d = deck.Deck(None)
    res = {}
    for c in d.cards:
        res[str(c)] = [0]*52
    return res

def fill_results(res, decks):
    for d in decks:
        cards = [str(c) for c in d.cards]
        for cardval in res.keys():
            res[cardval][cards.index(cardval)] += 1
    return res

def chisquare(test):
    #accumulate all the values
    values = []
    for vals in test.values():
        values += vals
    terms = [math.pow(x - 10, 2)/10 for x in values]
    return reduce(lambda x,y: x+y, terms, 0)

def run_test(shuffle):
    decks = []
    for i in xrange(520):
        d = deck.Deck(shuffle)
        d.shuffle(d)
        decks.append(d)
    return decks

# built in shuffle
res = initialise_results()
decks = run_test(deck.built_in_shuffle)
print("random module shuffle: " + str(chisquare(fill_results(res,decks))))

# manual shuffle
res = initialise_results()
decks = run_test(deck.manual_shuffle)
print("basic manual shuffle: " + str(chisquare(fill_results(res,decks))))

# odd-even  shuffle
res = initialise_results()
decks = run_test(deck.odd_even_shuffle)
print("odd-even shuffle: " + str(chisquare(fill_results(res,decks))))

# random swap shuffle
res = initialise_results()
decks = run_test(deck.random_swap_shuffle)
print("random swap shuffle: " + str(chisquare(fill_results(res,decks))))

