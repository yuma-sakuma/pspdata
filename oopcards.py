import random

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value,self.suit))
class Deck:
    def __init__(self):
        self.card = []
    def build(self):
        for s in ["Spades","Clubs","Diamods","Hearts"]:
            for v in range(1,14):
                self.card.append(Card(s,v))
    def show(self):
      for c in self.card:
        c.show()
    def firstDeal(self):
      return self.card.pop[0].show()
class Player():
  def __init__(self, card):
    self.randomcard = card
  def pickup(self):
    print(self.randomcard)

deck = Deck()
deck.build()
deck.show()
player = Player(deck.firstDeal())
player.pickup()