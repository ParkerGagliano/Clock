import time

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.isRunning=False

    def adjustTime(self):
        if self.seconds==60:
            self.seconds=0
            self.minutes+=1
        if self.minutes == 60:
            self.minutes=0
            self.hours+=1
        if self.hours == 24:
            self.hours=0
            self.minutes=0
            self.seconds=0

    def start(self):
        self.isRunning=True
        while self.isRunning:
            self.seconds+=1
            self.adjustTime()
            time.sleep(1)
            print(self.hours, self.minutes, self.seconds)

    def pause(self):
        self.isRunning=False

    
    def addOneSecond(self):
        time.sleep(.1)
        self.seconds+=1
        self.adjustTime()
        print(self.hours, self.minutes, self.seconds)

    def addTime(self, seconds):
        for i in range(seconds):
            self.addOneSecond()


