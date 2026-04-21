# Developed by @lucns

import time
from machine import Pin

class Button:
    def __init__(self, pin):
        self.button = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.lastState = 0
        self.changedTime = 0
        self.wasClicked = False

    def isPressed(self):
        return self.button.value() == 0

    def getState(self):
        ts = time.ticks_ms()
        pressed = self.isPressed()
        if pressed != self.lastState and ts - self.changedTime > 50: # debounce
            self.changedTime = ts
            if not pressed and self.lastState == 1:
                self.wasClicked = True
            self.lastState = pressed
        return self.lastState == 1

    def onClick(self):
        if not self.getState() and self.wasClicked:
            self.wasClicked = False;
            return True;  
        return False;