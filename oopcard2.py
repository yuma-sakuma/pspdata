import random

# class Game:
#     def __init__(self):
    
class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def showC(self):
        print(self.suit,self.value)
class Deck:
    def __init__(self):
        self.symbol = ['♠','♥','♦','♣']
        self.number = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.cardsID = []
        for i in self.symbol:
            for j in self.number:
                self.cardsID.append(Card(i,j))
        random.shuffle(self.cardsID)
    def drawcard(self):
        return self.cardsID.pop(0)
    def firstturn(self):
        return random.sample(self.cardsID,2)
    def show(self):
        for S in self.cardsID:
            S.showC()
        print(len(self.cardsID))
class Player:
    def __init__(self,card):
        self.cardsIH = card
    def checkCIH(self):
        print(self.cardsIH)
deck = Deck()
player = Player(deck.firstturn())
player.checkCIH()
#deck.show()
