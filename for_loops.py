# Circuit Playground For Loops
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE=(255,255,255)
OFF=(0,0,0)

wait = 0.5   #half second

while True:
    for i in range(0,10,1):    #basic for loop counting up by 1 from 0 to 9
        pixels[i] = (RED)
        pixels.show()
        time.sleep(wait)

    for i in range(0,10,2):   #basic for loop counting up by 2 from 0 to 9
        pixels[i] = (BLUE)
        pixels.show()
        time.sleep(wait)
    
    for j in range(0,255,1):   #basic for loop counting up by 1 from 0 to 254
        for i in range(10):    #nested for loop counting up by 1 from 0 to 9
            pixels[i] = (j,j,0)
            print ("i=%.0f,j=%.0f" % (i, j))
        pixels.show()
    time.sleep(wait)
       
    for j in range(255,0,-1):  #basic for loop counting down by 1 from  254 to 0
        for i in range(10):    #nested for loop counting up by 1 from 0 to 9
            pixels[i] = (j,j,0)
        pixels.show()
    time.sleep(wait)
