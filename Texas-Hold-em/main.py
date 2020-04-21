import Card
import Deck
import random

#Random Shuffle:

deck1 = Deck.Deck();
print('\n' + "Standard Deck:")
for val in deck1.deck:
    print("I have the " + val.name)
if(deck1.is_deck_valid()):
    print('\n'+"Our Deck is good:");

deck1.bridge_shuffle();
print('\n' + "Shuffle 1 Deck:")
for val in deck1.deck:
    print("I have the " + val.name)

if(deck1.is_deck_valid()):
    print('\n'+"Our Deck is good:");

    
