import random
class Game:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.valueP1 = 0
        self.valueP2 = 0
        self.powerP1 = 0
        self.powerP2 = 0
        if len(self.player1) == 3:
            if self.player1[0].suit == self.player1[1].suit == self.player1[2].suit:
                self.powerP1 += 2
            elif self.player1[0].suit == self.player1[1].suit or self.player1[1].suit == self.player1[2].suit or self.player1[1].suit == self.player1[2].suit:
                self.powerP1 += 1
        else:
            if self.player1[0].suit == self.player1[0].suit:
                self.powerP1 += 1
        if len(self.player2) == 3:
            if self.player2[0].suit == self.player2[1].suit == self.player2[2].suit:
                self.powerP2 += 2
            elif self.player2[0].suit == self.player2[1].suit or self.player2[1].suit == self.player2[2].suit or self.player2[1].suit == self.player2[2].suit:
                self.powerP2 += 1
        else:
            if self.player2[0].suit == self.player2[0].suit:
                self.powerP2 += 1
        for i in self.player1:
            if i.value == "K" or i.value == "Q" or i.value == "J":
                self.valueP1 += 0
            else:
                self.valueP1 += i.value
        for j in self.player2:
            if j.value == "K" or j.value == "Q" or j.value == "J":
                self.valueP2 += 0
            else:
                self.valueP2 += j.value
        while self.valueP1 >= 10:
            self.valueP1 -= 10
        while self.valueP2 >= 10:
            self.valueP2 -= 10
    def dual(self):
        if self.valueP1 > self.valueP2:
            if len(self.player1) == 3:
                print("Player 1 win : {}{} , {}{} , {}{}".format(self.player1[0].value,self.player1[0].suit,self.player1[1].value,self.player1[1].suit,self.player1[2].suit,self.player1[2].value))
            else:
                print("Player 1 win : {}{} , {}{}".format(self.player1[0].value,self.player1[0].suit,self.player1[1].value,self.player1[1].suit))
        elif self.valueP2 > self.valueP1:
            if len(self.player1) == 3:
                print("Player 1 win : {}{} , {}{} , {}{}".format(self.player1[0].value,self.player1[0].suit,self.player1[1].value,self.player1[1].suit,self.player1[2].suit,self.player1[2].value))
            else:
                print("Player 2 win : {}{} , {}{}".format(self.player2[0].value,self.player2[0].suit,self.player2[1].value,self.player2[1].suit))
        elif self.valueP1 == self.valueP2:
            print("Draw")
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
            S.showS()
            S.showV()
        print(len(self.cardsID))
class Player:
    def __init__(self,name,card):
        self.player_name = name
        self.cardsIH = card
    def checkCIH(self):
        for i in self.cardsIH:
            i.showS()
            i.showV()
    def drawcard(self,drawcard):
        self.cardsIH.append(drawcard)
    def cardsInHand(self):
        return self.cardsIH
deck = Deck()
p1 = input("Enter name Player 1 : ")
p2 = input("Enter name Player 2 : ")
player1 = Player(p1,deck.firstturn())
player2 = Player(p2,deck.firstturn())
print("{} card : {}".format(player1.player_name,player1.cardsIH))
drawcardP1 = input("Do you want to draw card? : ")
if drawcardP1 == "Yes":
    player1.drawcard()
    print("Player1 has draw {}".format(player1.cardsIH))
    print("Turn player 2")
else:
    print("Turn player 2")
print("{} card : {}".format(player2.player_name,player2.cardsIH))
drawcardP2 = input("Do you want to draw card? : ")
if drawcardP2 == "Yes":
    player2.drawcard()
    print("Player2 has draw {}".format(player1.cardsIH))
    print("Dual!!!")
else:
    print("Dual!!!")
game = Game(player1.cardsInHand(),player2.cardsInHand())
game.dual()