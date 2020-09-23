# Circuit Playground Temperature
# Reads the on-board temperature sensor and prints the value
# turns red over 26 C
 
import time
import adafruit_thermistor
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)
 
thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)
    
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (255,0,0)
OFF = (0,0,0)
 
while True:
    temp_c = thermistor.temperature
    temp_f = thermistor.temperature * 9 / 5 + 32
    print("Temperature is: %f C and %f F" % (temp_c, temp_f))
    
    if temp_c >= 26:
        pixels.fill(RED)   #turn on all pixels
        pixels.show()
    else:
        pixels.fill(OFF)   #turn on all pixels
        pixels.show()

    time.sleep(0.25)
