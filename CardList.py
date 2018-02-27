from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

from random import randint


class CardList():

    def __init__(self):
        '''Initializes the CardList with a starting size of 0'''
        self.CurrentSize = 0
        self.Cards = none



    def __repr__(self):
        '''Returns the String of the Names of the Cards in the hand object'''
        s = ''
        if self.Cards == None:
            return s
        for Card in self.Cards:
            s+= Card.name + "\n"
        return s

    def add_card(self,Card):
        '''Should pass in a Card, not a string representation of a Card'''
        if self.Cards == None:
            self.Cards = [Card]
            self.CurrentSize +=1
            return
    else:
            self.Cards.append(Card)
            self.CurrentSize +=1

    def add_cards(self,Cards):
        for Card in Cards:
            self.add_card(Card)

    def remove_card(self, Card):
        '''Should pass in a Card, not a string representation of a Card'''
        if self.Cards == None:
            print("This doesn't have any cards")
        else:
            if Card in self.Cards:
                self.Cards.pop(Card)
                self.CurrentSize -=1
            else:
                print("Card is not in the Set")

    def remove_random_card(self):
        if self.Cards == None:
            print("This doesn't have any cards")
        else:
            self.Cards.pop(randint(0,CurrentSize))
            self.CurrentSize-=1


myHand = CardList()
myHand.add_cards([Card.find(386616), Card.find(386617)])
myHand.add_card(Card.find(386618))
myHand.add_card(Card.find(386619))
myHand.add_card(Card.find(386620))
myHand.add_card(Card.find(386615))
myHand.add_card(Card.find(386614))
print(myHand)


print("-----------")
#intentionally adding an extra card to test what will happen
myHand.add_card(Card.find(386614))
for card in myHand:
    print(card.type)
