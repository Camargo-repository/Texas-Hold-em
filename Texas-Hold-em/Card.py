class Card(object):
    """ Basic Playing Card for poker:
        Suit: 1 = Spades, 2 = Clubs, 3 = Hearts, 4 = Diamonds
        Value: 1 = Ace, 2-10 = themselves, 11 = Jack, 12 = Queen, 
                13 = King
    """

    def __init__(self, suit: int, val: int):
        self.suit = suit;
        self.value = val;

        #Maps suit num to string
        suit_name = {
            1: "Spades",
            2: "Clubs",
            3: "Diamonds",
            4: "Hearts",
       }
        #Maps val num to string
        val_name = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        self.name = val_name.get(val, "Invalid Value") + " of " + suit_name.get(suit, "Invalid Suit");

    #getters
    def get_name(): return name;
    def get_suit(): return suit;
    def get_value(): return value;

    #setters
    def set_name(word): self.name = word;
    def set_suit(num): self.suit = num;
    def set_value(val): self.value = val;


        #    def suit_switch(arg):
#       switcher = {
#            1: "Spades",
#            2: "Clubs",
#            3: "Diamonds",
#            4: "Hearts",
#       }
#        print(switcher.get(arg, "Invalid Suit"))

#    def val_switch(arg):
#        switcher = {
#            1: "Ace",
#            2: "Two",
#            3: "Three",
#            4: "Four",
#            5: "Five",
#            6: "Six",
#            7: "Seven",
#            8: "Eight",
#            9: "Nine",
#            10: "Ten",
#            11: "Jack",
#            12: "Queen",
#            13: "King"
#        }
#        print(switcher.get(arg,"Invalid value"));


      
        


