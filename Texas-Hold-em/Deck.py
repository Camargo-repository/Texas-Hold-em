import Card
import random

class Deck(object):
    """ Collection of 52 self:
            13 self of the four suits
    """
    deck = [];
    def __init__(self):
        for i in range(1,5):
            for j in range(1,14):
                self.deck.append(Card.Card(i,j));
    def len(list):
        length = 0;
        for i in list:
            length = length + 1;
        return length;

    #Bridge Shuffle: cut deck in half and then, put bottom of 
    def bridge_shuffle(self):
        length = len(self.deck);
        half_1 = [];
        half_2 = [];

        for i in range(0,length):
            if(i < length/2):#upper half
                half_1.append(self.deck[i]);
            else: #lower half
                half_2.append(self.deck[i]);
        
        h1_index = 0;
        h2_index = 0;
        self.deck.clear();
        for i in range(0,length):
            if(i % 2 == 0): #even
                self.deck.append(half_1[h1_index]);
                h1_index = h1_index + 1;
            else: #odd
                self.deck.append(half_2[h2_index]);
                h2_index = h2_index + 1;
    
    #Random Shuffle: Moves
    def random_shuffle(self):
        temp = self.deck.copy();
        length = len(self.deck);
        self.deck.clear()
        
        for val in range(0,length):
            self.deck.append(temp.pop(random.randint(0,len(temp)-1)));

    #Checks if the deck has a standard amount of self & suits
    def is_deck_valid(self):
        suit_dict = {1:0,2:0,3:0,4:0};
        val_dict = {1:0, 2:0, 3:0, 4:0,
                    5:0, 6:0, 7:0, 8:0,
                    9:0, 10:0, 11:0, 12:0,
                    13:0};
        length = len(self.deck)
        for i in range(0,length):
            suit_dict[self.deck[i].suit] = suit_dict[self.deck[i].suit]+1;
            val_dict[self.deck[i].value] = val_dict[self.deck[i].value]+1;
            if(suit_dict[self.deck[i].suit] > 13):
                return False;
            if(val_dict[self.deck[i].value] > 4):
                return False;
        return True;