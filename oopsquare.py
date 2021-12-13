import random

small_long = random.randint(1,5)
small_wide = random.randint(1,5)

class Small_square():
    def __init__(self):
        self.square = small_long * small_wide
    def check_area(self,player_area):
        if  player_area == self.square :
            print("おめでとう！")
        else:
            print("頑張って、死ね")
            print("ขนาดของสี่เหลี่ยม : {}".format(self.square))

player_area = int(input("ลองเดาขนาดสี่เหลี่ยมดูสิ (1-25) : "))
small_square = Small_square()
small_square.check_area(player_area)