import time
import threading
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
        time.sleep(.02)
        self.seconds+=1
        self.adjustTime()
        print(self.hours, self.minutes, self.seconds)

currentTime = time.ctime(time.time())[-14:-5]
print(type(currentTime))
def convertTime(a):
    hours=int(a[0:3])
    minutes=int(a[4:6])
    seconds=int(a[7:9])
    return[hours, minutes, seconds]


def test(a):
    a.pause()
    for i in range(100):
        a.addOneSecond()
c = Clock(22, 9, 1)
clock_thread = threading.Thread(target=c.start)
clock_thread.start()
time.sleep(5)
test(c)
clock_thread.join()

