#dice example
from adafruit_circuitplayground import cp
import time
import random


def dice():
    roll=() #create randomization here
    if (roll==1):       #here's a one but you need 6 combos for a dice
        cp.pixels[2]=(50, 0, 0) 
    time.sleep(3.0)
    cp.pixels.fill((0, 0, 0))
    
while True:
    if:    #use the shake example code here
        dice()
        cp.red_led = True
        
    else:
        cp.red_led = False
