from Graveyard import Graveyard
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

class CreatureCard(Card):
    def __init__(self):
    '''initializes the Creatures power and toughness'''
        self.power = Card.power
        self.toughness = Card.toughness
