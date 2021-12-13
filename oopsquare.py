import random

long = random.randint(1,5)
wide = random.randint(1,5)

class Square():
    def __init__(self):
        global long,wide
        self.square = long * wide
    def check_area(self,player_area):
        if  player_area == self.square :
            print("おめでとう！")
        else:
            print("頑張って 死ね")
            print("ขนาดของสี่เหลี่ยมก็คือ",self.square)

player_area = int(input("ลองเดาขนาดสี่เหลี่ยมดูสิ (1-25) : "))
small_square = Square()
small_square.check_area(player_area)