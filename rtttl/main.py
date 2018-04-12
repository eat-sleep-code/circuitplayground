from random import *
import board
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

song = "d=16,o=6,b=240:8g#5,p,8g#5,p,8b5,p,4d#,p,2c#.,p,2g#5.,p,8g#5,p,8g#5,p,8f#5,p,4b5,p,1g#5,4p.,8g#5,p,8g#5,p,8b5,p,4d#,p,2c#,8p,2g#.,8p,8f#,p,8f#,p,8d#,p,4b5,p,1g#.,4p,2b,p,8a,8g#,8f#,8e,8d#,8c#,8d#,8b5,2c#,4p,8c#,p,8b,8a,8g,8f#,8d#,8c#,8b5,8c#,4d#,8c#,p,4b5,p,4c#.,p,2g#,4p,8f#,p,8f#,p,8d#,p,4b5,p,1c#6"

notes = song.split(",")
for (var i - 0; i < notes.length; i++) {
    TurnOffPixels()
    currentNote = notes[i];
    redValue = random.randint(128,255)
    greenValue = random.randint(128,255)
    blueValue = random.randint(128,255)
    print(currentNote)
    if "a" in currentNote: 
        pixels[0] = (redValue, greenValue, blueValue)
    else if "b" in currentNote: 
        pixels[1] = (redValue, greenValue, blueValue)
    else if "c" in currentNote: 
        pixels[2] = (redValue, greenValue, blueValue)
    else if "d" in currentNote: 
        pixels[3] = (redValue, greenValue, blueValue)
    else if "e" in currentNote: 
        pixels[4] = (redValue, greenValue, blueValue)
    else if "f" in currentNote:
        pixels[5] = (redValue, greenValue, blueValue) 
    else if "g" in currentNote: 
        pixels[6] = (redValue, greenValue, blueValue)  
    else:      
        pixels[7] = (redValue, greenValue, blueValue)
    pixels.show()
    adafruit_rtttl.play(board.A2, "Note:" + currentNote)    
}
TurnOffPixels()
