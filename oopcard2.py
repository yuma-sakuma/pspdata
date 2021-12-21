import random

class Game:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
    
        
class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def showS(self):
        return self.suit
    def showV(self):
        return self.value
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
        for i in self.cardsIH:
            i.showC()
    def drawcard(self,drawcard):
        self.cardsIH.append(drawcard)
    def cardsInHand(self):
        return self.cardsIH
deck = Deck()
player1 = Player(deck.firstturn())
player2 = Player(deck.firstturn())
game = Game(player1.cardsInHand(),player2.cardsInHand())
player1.checkCIH()
player2.checkCIH()
game.dual()


#deck.show()
#player.drawcard(deck.drawcard())
#player.checkCIH()