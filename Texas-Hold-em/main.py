import Card
import Deck
import random

deck1 = Deck.Deck();
print('\n' + "Standard Deck:")
for val in deck1.deck:
    print("I have the " + val.name)
if(deck1.is_deck_valid()):
    print('\n'+"Our Deck is good:");

deck1.random_shuffle();
print('\n' + "Shuffle 1 Deck:");
for val in deck1.deck:
    print("I have the " + val.name)
if(deck1.is_deck_valid()):
    print('\n'+"Our Deck is good:");

deck1.bridge_shuffle();
print('\n' + "Shuffle 2 Deck:")
for val in deck1.deck:
    print("I have the " + val.name);
if(deck1.is_deck_valid()):
    print('\n'+"Our Deck is good:");

