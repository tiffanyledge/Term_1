import random
class Player:
    def __init__(self, limit_L, limit_R, sense):
        self.limit_L = limit_L
        self.limit_R = limit_R
        self.sense = sense
        self.position = random.randint(limit_L, limit_R) 
    def move_right(self): 
        if self.position < self.limit_R:
            self.position = self.position + 1
            self.display(1)

    def move_left(self):
        if self.position > self.limit_L:
            self.position = self.position - 1
            self.display(-1)

    def display(self, move):
        x = self.position % 8
        self.sense.set_pixel(x-move, 7, (0,0,0))
        self.sense.set_pixel(x, 7, (255,255,255))