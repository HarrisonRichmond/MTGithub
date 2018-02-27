from CardList import CardList
from Player import Player
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

class side():
    '''The idea for this class is to make one complete side of the board. Each side should have a mana pool
    and a '''
    def __init__(self):
        self.battlefield = CardList()
        self.manapool = CardList()
        self.Deck = CardList()
        self.Graveyard= CardList()
        self.Player = Player()
