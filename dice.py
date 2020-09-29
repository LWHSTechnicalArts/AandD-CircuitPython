#dice example
from adafruit_circuitplayground import cp
import time
import random


def dice():
    roll=random.randint(1, 6)
    if (roll==1):    
        cp.pixels[2]=(50, 0, 0)
    elif (roll==2):
        cp.pixels[2]=(50, 0, 0)
        cp.pixels[7]=(50, 0, 0)
    elif (roll==3):
        cp.pixels[2]=(50, 0, 0)
        cp.pixels[4]=(50, 0, 0)
        cp.pixels[8]=(50, 0, 0)
    elif (roll==4):
        cp.pixels[1]=(50, 0, 0)
        cp.pixels[3]=(50, 0, 0)
        cp.pixels[6]=(50, 0, 0)
        cp.pixels[8]=(50, 0, 0)
    elif (roll==5):
        cp.pixels[0]=(50, 0, 0)
        cp.pixels[2]=(50, 0, 0)
        cp.pixels[4]=(50, 0, 0)
        cp.pixels[6]=(50, 0, 0)
        cp.pixels[8]=(50, 0, 0)
    elif (roll==6):
        cp.pixels[0]=(50, 0, 0)
        cp.pixels[2]=(50, 0, 0)
        cp.pixels[4]=(50, 0, 0)
        cp.pixels[5]=(50, 0, 0)
        cp.pixels[7]=(50, 0, 0)
        cp.pixels[9]=(50, 0, 0)
    time.sleep(3.0)
    cp.pixels.fill((0, 0, 0))
    
while True:
    if cp.shake(shake_threshold=20):
        print("Shake detected!")
        dice()
        cp.red_led = True
        
    else:
        cp.red_led = False
