import random

small_x1 = random.randint(0,10)
small_y1 = random.randint(0,10)
small_x2 = small_x1 + random.randint(5,10)
small_y2 = small_y1 + random.randint(5,10)

class Small_square():
    def __init__(self):
        self.small_x1 = small_x1
        self.small_y1 = small_y1
        self.small_x2 = small_x2
        self.small_y2 = small_y2
    def check_xy(self,player_x,player_y):
        if self.small_x1 < player_x < self.small_x2 and self.small_y1 < player_y < self.small_y2 :
            print("おめでとう！")
        else:
            print("頑張って、死ね")

player_x = int(input("ค่า x ของคุณที่คุณจะทาย : "))
player_y = int(input("ค่า y ของคุณที่คุณจะทาย : "))

small_square = Small_square()
small_square.check_xy(player_x,player_y)