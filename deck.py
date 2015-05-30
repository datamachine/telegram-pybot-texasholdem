from random import shuffle
from enum import Enum


class Suit(Enum):
    hearts = 1
    diamonds = 2
    spades = 3
    clubs = 4


class Card:
    def __init__(self, suit, value)
        self.suit = suit
        self.value = value

    def __str__(self):
        text = ""

        # Value
        try:
            text = {
                    11: 'J',
                    12: 'Q',
                    13: 'K',
                    14: 'A'
            } [self.value]
        except KeyError:
            text = str(self.value)

        # Suit
        text += {
            Suit.hearts: b'\xe2\x99\xa5\xef\xb8\x8f',
            Suit.diamonds: b'\xe2\x99\xa6\xef\xb8\x8f',
            Suit.spades: b'\xe2\x99\xa0\xef\xb8\x8f',
            Suit.clubs: b'\xe2\x99\xa3\xef\xb8\x8f'
        } [self.suit].decode('utf-8')

class Deck:
    def __init__(self):
        self.cards = []
        self.inplay = []

        for suit in Suit:
            for value in range(2, 15)
                self.cards.append( Card(suit, value) )

        self.total_cards = 52

    def shuffle(self)
        self.cards.extend( self.inplay )
        self.inplay = []
        shuffle( self.cards )

    def deal(self, number_of_cards):
        if(number_of_cards > len(self.cards) ):
            return False # Not enough cards
        inplay = []
        for i in range(0, number_of_cards):
            inplay.append( self.cards.pop(0) )

         self.inplay.extend(inplay)
         return inplay

    def cards_left(self):
        return len(self.cards)
