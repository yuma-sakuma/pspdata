import random
class Game:
    def __init__(self,player1,player2):
        self.cardplayer1 = player1
        self.cardplayer2 = player2
        self.numberCP1 = 0
        self.numberCP2 = 0
    def checkscore(self):
        for i in self.cardplayer1:
            if i[0] == "J" or i[0] == "Q" or i[0] == "K" or i[0] == "10":
                self.numberCP1 += 0
            else:
                self.numberCP1 += int(i[0])
                if self.numberCP1 >= 10:
                    self.numberCP1 -= 10
        for i in self.cardplayer2:
            if i[0] == "J" or i[0] == "Q" or i[0] == "K" or i[0] == "10":
                self.numberCP2 += 0
            else:
                self.numberCP2 += int(i[0])
                if self.numberCP2 >= 10:
                    self.numberCP2 -= 10
    def dualru(self):
        if self.numberCP1 > self.numberCP2 or self.P1suitsame > self.P2suitsame and not self.P1suitsame < self.P2suitsame:
            print(self.numberCP1,self.numberCP2,self.P1suitsame,self.P2suitsame)
            print("player 1 win")
        elif  self.numberCP1 < self.numberCP2 or self.P1suitsame < self.P2suitsame and not self.P1suitsame > self.P2suitsame:
            print(self.numberCP1,self.numberCP2,self.P1suitsame,self.P2suitsame)
            print("player 2 win")
        else:
            print("always score")
        
class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
class Deck:
    def __init__(self):
        self.symbol = ['♠','♥','♦','♣']
        self.number = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.cards = []
        for i in self.symbol:
            for j in self.number:
                self.cards.append(Card(i)(j))
        random.shuffle(self.cards)
    def drawcard(self):
        return self.cards.pop(0)
class Player():
    def __init__(self):
        self.playercardsinhand = []
    def drawCTD(self,drawcard):
        self.playercardsinhand.append(drawcard)
    def checkCIH(self):
        print(self.playercardsinhand)
    def dual(self):
        return self.playercardsinhand
deck = Deck()
player1 = Player()
player2 = Player()
gamestart = Game(player1.dual(),player2.dual())
player1.drawCTD(deck.drawcard())
player1.drawCTD(deck.drawcard())
player2.drawCTD(deck.drawcard())
player2.drawCTD(deck.drawcard())
player1.checkCIH()
player2.checkCIH()
gamestart.checkscore()
gamestart.checksuit()
gamestart.dualru()