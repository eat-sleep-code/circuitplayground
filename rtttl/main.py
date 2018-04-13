import board
import random
from digitalio import DigitalInOut, Direction
import neopixel
import adafruit_rtttl

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)
pixelCount = len(pixels)

speaker = DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = Direction.OUTPUT
speaker.value = True

def TurnOffPixels():
    for s in range(pixelCount): 
        pixels[s] = (0, 0, 0)
        pixels.show()
    return True

song = "d=4,o=4,b=160:8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5,8f#5,8e5,8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5"

songConfig = song.split(":")[0]
songNotes = song.split(":")[1].split(",")
for i in range(0, len(songNotes) - 1):
    #TurnOffPixels()
    currentNote = songNotes[i]
    redValue = random.randint(0,255)
    greenValue = random.randint(0,255)
    blueValue = random.randint(0,255)
    #print(currentNote)
    if "a" in currentNote: 
        pixels[1] = (redValue, greenValue, blueValue)
    elif "b" in currentNote: 
        pixels[2] = (redValue, greenValue, blueValue)
    elif "c" in currentNote: 
        pixels[3] = (redValue, greenValue, blueValue)
    elif "d" in currentNote: 
        pixels[4] = (redValue, greenValue, blueValue)
    elif "e" in currentNote: 
        pixels[5] = (redValue, greenValue, blueValue)
    elif "f" in currentNote:
        pixels[6] = (redValue, greenValue, blueValue) 
    elif "g" in currentNote: 
        pixels[7] = (redValue, greenValue, blueValue)  
    else:      
        pixels[8] = (redValue, greenValue, blueValue)
    pixels.show()
    adafruit_rtttl.play(board.A0, "Note:" + songConfig + ":" + currentNote)    
TurnOffPixels()
