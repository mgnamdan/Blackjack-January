from cards import Card
from random import shuffle


class Deck:

    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    SUITS = ["Clubs", "Diamonds", "Spades", "Hearts"]

    def __init__(self):
        self.drawPile = []
        self.discardPile = []
        self.outPile = []
        self.setupDrawPile()


    def setupDrawPile(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                newCard = Card(rank, suit)
                self.drawPile.append(newCard)

    
    def __repr__(self):
        return "\n".join(str(card) for card in self.drawPile)
    

    def __eq__(self, other):
        pass


    def draw(self):
        drawnCard = self.drawPile.pop(0)
        self.outPile.append(drawnCard)
        return drawnCard


    def discard(self, card):
        returnedCard = card
        self.outPile.remove(returnedCard)
        self.discardPile.append(returnedCard)


    def deckShuffle(self):
        shuffle(self.drawPile)