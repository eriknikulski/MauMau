import random

import card

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['C', 'D', 'H', 'S']


class Deck:
    __cards = []
    __discards = []

    def __init__(self):
        for suit in SUITS:
            for rank in RANKS:
                self.__cards.append(card.Card(suit, rank))
        self.shuffle()
        self.__discards = [self.__cards.pop()]

    def shuffle(self):
        random.shuffle(self.__cards)

    def draw(self) -> card.Card:
        if len(self.__cards) > 0:
            return self.__cards.pop()
        else:
            d = self.__discards.pop()
            self.__cards = self.__discards
            self.shuffle()
            self.__discards = [d]
            return self.__cards.pop()

    def discard(self, card : card.Card):
        self.__discards.append(card)

    def get_last_discard(self) -> card.Card:
        return self.__discards[-1]
