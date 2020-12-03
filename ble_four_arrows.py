from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket

import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Now we're connected

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.LEFT:
                        # The 1 button was pressed.
                        print("1 button pressed!")
                        pixels.fill(BLUE)
                        pixels.show()
                    elif packet.button == ButtonPacket.UP:
                        # The UP button was pressed.
                        print("UP button pressed!")
                        pixels.fill(RED)
                        pixels.show()
                    elif packet.button == ButtonPacket.DOWN:
                        # The UP button was pressed.
                        print("DOWN button pressed!")
                        pixels.fill(GREEN)
                        pixels.show()
                    elif packet.button == ButtonPacket.RIGHT:
                        # The UP button was pressed.
                        print("DOWN button pressed!")
                        pixels.fill(YELLOW)
                        pixels.show()


    # If we got here, we lost the connection. Go up to the top and start
    # advertising again and waiting for a connection.
