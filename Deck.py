from CardList import CardList
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
from random import shuffle

class Deck(CardList):
    '''Mostly inherits from the CardList class. This is one of the only Cardlists that order matters'''
    def shuffle(self):
        shuffle(self.Cards)

    def add_card_to_top(self, Card):
        self.Cards.insert(0, Card)

$$    def remove_basic(self, color)
'''To do: find out what each different basic mana looks like and use the CardList remove functionality'''
