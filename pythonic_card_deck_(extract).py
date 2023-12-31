# -*- coding: utf-8 -*-
"""
Fluent Cards list with Magic Function: __getitem__
"""
import collections;
from random import choice;

Card = collections.namedtuple('Card', ['rank', 'suit']);

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA');
    suits = 'spades diamonds clubs hearts'.split();
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks];
    
    def __len__(self):
        return len(self._cards);
    
    def __getitem__(self, position):
        return self._cards[position];

if __name__ == "__main__":
    beer_card =Card ('5', 'clubs');
    print(beer_card)
    print(len(FrenchDeck()))
    print(choice(FrenchDeck()))
    print(FrenchDeck()[12::13])