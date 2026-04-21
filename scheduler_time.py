import time

class Scheduler:

    def __init__(self):
        self.scheduledTime = 0
    
    def schedule(self, seconds):
        self.scheduledTime = time.ticks_ms() + (seconds * 1000)

    def getTime(self):
        t = int((self.scheduledTime - time.ticks_ms()) / 1000)
        if t < 0: t = 0
        return t

    def thrigger(self):
        return time.ticks_ms() >= self.scheduledTime