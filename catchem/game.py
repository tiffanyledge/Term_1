from sense_hat import SenseHat
import random
import time
from player import Player
from berries import Berry
sense = SenseHat()
colors = (255, 255, 255)


class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.speed = 0.5
        self.berry = Berry((255,255,255),.5,10)
        self.player = Player(56,63,sense)
    def start(self):
        sense.show_message("Catchem !", text_colour=colors, scroll_speed=0.05)
        
        
    def play(self):
        self.start()
        self.player.display(0)
        self.berry.display()
        while not self.game_over:
            self.berry.drop()
            #sleep(speed)
            time.sleep(.5)	
            self.berry.display()  
            for event in sense.stick.get_events():
                if event.action == "pressed" and event.direction == "left":
                    print("left")
                    self.player.move_left()
                elif event.action == "pressed" and event.direction == "right":
                    print("right")
                    self.player.move_right()

        


