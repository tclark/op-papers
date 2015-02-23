#! /usr/bin/python
import sys
import deck
import player


d = deck.Deck()
p = player.Player()
h = player.HousePlayer()
p.take_card(d.next())
h.take_card(d.next())
p.take_card(d.next())
h.take_card(d.next())

print("House: " + h.show_hand_hidden_down())
print("You: " + p.show_hand())

print("Your play")
while(p.hits()):
    p.take_card(d.next())
    print("House: " + h.show_hand_hidden_down())
    print("You: " + p.show_hand())
    print("==========")
    if(p.score() > 21):
        print("Busted!")
        sys.exit()
    print("")

print("")
print("House plays")
print("House: " + h.show_hand())
print("You: " + p.show_hand())
print("==========")
print("")
while(h.hits()):
    h.take_card(d.next())
    print("House: " + h.show_hand())
    print("You: " + p.show_hand())
    print("==========")
    if(h.score() > 21):
        print("Busted!")
        sys.exit()
    print("")

if(p.score() > h.score()):
    print("You win")
else:
    print("House wins")
