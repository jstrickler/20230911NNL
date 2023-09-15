from dataclasses import dataclass
import random

@dataclass
class Card:
    rank: str
    suit: str
    color: str

# class Card:
#     def __init__(self, rank, suit):
#         self._rank = rank
#         self._suit = suit

#     @property
#     def rank(self):
#         return self._rank
    
#     @property
#     def suit(self):
#         return self._suit
    
#     def __str__(self):  # human-friendly
#         return f"{self.rank}-{self.suit}"

#     def __repr__(self):  # code representation
#         return f"Card('{self.rank}', '{self.suit}')"

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    
    def __init__(self, dealer):
        self._dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                suit_color = 'red' if suit in ('Diamonds', 'Hearts') else 'black'
                card = Card(rank, suit, suit_color)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop(0)

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, name):
        if isinstance(name, str):
            self._dealer = name
        else:
            raise TypeError("Dealer must be a str")

    def __len__(self):
        return len(self._cards)

    def _get_class_name(self):
        my_type = type(self)
        return my_type.__name__

    #  "CardDeck-42-Dealer"
    def __str__(self):
        return f"{self._get_class_name()}-{self.dealer}-{len(self)}"
    
    #  CardDeck("Dealername")
    def __repr__(self):
        return f"""{self._get_class_name()}("{self.dealer}")"""

    def __add__(self, other):
        tmp_deck = type(self)(self.dealer)
        tmp_deck._cards = self._cards + other._cards
        return tmp_deck

    @classmethod
    def get_ranks(cls):
        return tuple(cls.RANKS)

    @property
    def cards(self):
        return self._cards

if __name__ == "__main__":
    d1 = CardDeck()

    c1 = Card('2', 'Diamonds')
    print(c1.rank, c1.suit)
    print(f"c1: {c1}")
    print(f"repr(c1): {repr(c1)}")
    