from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
from random import *
import board
import neopixel
import time

# Initialize LEDs
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)
pixels.fill((0,0,0))
pixels.show()
pixelCount = len(pixels)

# Setup button(s)
leftButton = DigitalInOut(board.BUTTON_A)
leftButton.direction = Direction.INPUT
leftButton.pull = Pull.DOWN

rightButton = DigitalInOut(board.BUTTON_B)
rightButton.direction = Direction.INPUT
rightButton.pull = Pull.DOWN

slideSwitch = DigitalInOut(board.SLIDE_SWITCH)
slideSwitch.direction = Direction.INPUT
slideSwitch.pull = Pull.UP

# Setup analog
triggerIn = AnalogIn(board.A1)
triggerOut = AnalogOut(board.A0)

def GetVoltage(pin):
    voltage = (pin.value * 3.3) / 65536
    # print (str(voltage))
    return voltage

def MakeRedLeft():
    for p in range(pixelCount / 2):
        pixels[p] = (255, 0, 0)
    return True

def MakeBlueLeft():
    for p in range(pixelCount / 2):
        pixels[p] = (0, 0, 255)
    return True

def MakeRedRight():
    for p in range(pixelCount / 2):
        pixels[(pixelCount - 1) - p] = (255, 0, 0)
    return True

def MakeBlueRight():
    for p in range(pixelCount / 2):
        pixels[(pixelCount - 1) - p] = (0, 0, 255)   
    return True

def TurnOffPixels():
    for s in range(pixelCount): 
        pixels[s] = (0, 0, 0)
        pixels.show()
    return True

def LightPixels(voltageTriggered): 
    while not rightButton.value:
        voltage = GetVoltage(triggerIn)
        if (voltageTriggered == True and voltage < 2.5):
            print("Voltage: " + str(voltage) + " (OFF)")
            triggerOut.value = 0
            return False
        else:
            triggerOut.value = 65535
        for i in range(randint(3, 5)):
            MakeRedLeft()
            MakeBlueRight()
            pixels.show()
            time.sleep(0.02)
            MakeBlueLeft()
            MakeRedRight()
            pixels.show()
            time.sleep(0.02)
        # TurnOffPixels()
        for i in range(randint(3, 5)):
            for p in range(randint(1,9)):
                pixels[randint(0, 9)] = (255, 255, 255)
                pixels.show()
            time.sleep(0.02)
            TurnOffPixels()
            
while True:
    voltage = GetVoltage(triggerIn)
    if (rightButton.value):
        print("Right button pressed (OFF)")
        triggerOut.value = 0
    elif (voltage > 2.5):
        print("Voltage: " + str(voltage) + " (ON)")
        LightPixels(True)
    elif (leftButton.value):
        print("Left button pressed (ON)")
        LightPixels(False)
