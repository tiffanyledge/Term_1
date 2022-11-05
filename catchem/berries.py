import random
from sense_hat import SenseHat



sense = SenseHat()
class Berry:
    def __init__(self, color, speed, value):
        self.color = (255,255,255)
        self.speed = 1
        self.value = 1
        self.posx = random.randint(0,7)
        self.berry = []     
        self.posy = 1
       
    def display(self):
        x = self.posx
        y = self.posy
        sense.set_pixel(x,(y-1), (0,0,0))
        sense.set_pixel(x,y ,(255,255,255))
    
    def drop(self):
        if self.posy >= 0 and self.posy < 7:
            self.posy +=1 
            self.display()

