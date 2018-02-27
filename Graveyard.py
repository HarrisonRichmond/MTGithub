from CardList import CardList
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog


class Graveyard(CardList):




myHand = Graveyard()
myHand.add_cards([Card.find(386616), Card.find(386617)])
myHand.add_card(Card.find(386618))
myHand.add_card(Card.find(386619))
myHand.add_card(Card.find(386620))
myHand.add_card(Card.find(386615))
myHand.add_card(Card.find(386614))
print(myHand)
