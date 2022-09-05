import time
import turtle

class Clock:
    def __init__(self, hours, minutes, seconds, pen, wn):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.isRunning=False
        self.pen = pen
        self.wn = wn

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

    def render(self):
        self.pen.clear()
        self.draw_clock()
        self.wn.update()

    def start(self):
        self.isRunning=True
        while self.isRunning:
            self.seconds+=1
            self.adjustTime()
            self.render()
            time.sleep(1)
            print(self.hours, self.minutes, self.seconds)

    def pause(self):
        self.isRunning=False

    def draw_clock(self):
        self.pen.up()
        self.pen.goto(0, 210)
        self.pen.setheading(180)
        self.pen.color('green')
        self.pen.pendown()
        self.pen.circle(210)

        self.pen.penup()
        self.pen.goto(0,0)
        self.pen.setheading(90)

        for _ in range(12):
            self.pen.fd(190)
            self.pen.pendown()
            self.pen.fd(20)
            self.pen.penup()
            self.pen.goto(0,0)
            self.pen.rt(30)

        # hour hand
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color('orange')
        self.pen.setheading(90)
        self.angle = (self.hours/ 12) * 360
        self.pen.rt(self.angle)
        self.pen.pendown()
        self.pen.fd(100)

        # minute hand
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color('red')
        self.pen.setheading(90)
        self.angle = (self.minutes/ 60) * 360
        self.pen.rt(self.angle)
        self.pen.pendown()
        self.pen.fd(140)

        # second hand
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color('orange')
        self.pen.setheading(90)
        self.angle = (self.seconds/ 60) * 360
        self.pen.rt(self.angle)
        self.pen.pendown()
        self.pen.fd(180)
