import time
import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analog clock")
wn.tracer(0)

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

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
        #self.draw_clock(pen)
        #wn.update()
        while self.isRunning:
            turtle.onkey(self.keyPress,'space')
            self.seconds+=1
            self.adjustTime()
            self.draw_clock(pen)
            #if self.isRunning:
            wn.update()
            pen.clear()
            time.sleep(1)
            print(self.hours, self.minutes, self.seconds)

    def pause(self):
        self.isRunning=False
        

    
    def keyPress(self):
        self.isPressed=True
        self.pause()
        while self.isPressed:
            #self.addOneSecond()
            turtle.onkeypress(self.keyRelease, "a")

    def keyRelease(self):
        self.isPressed=False
        self.start()

    def addOneSecond(self):
        time.sleep(.1)
        self.seconds+=1
        self.adjustTime()
        self.draw_clock(pen)
        wn.update()
        pen.clear()
        print(self.hours, self.minutes, self.seconds)

    def addTime(self, seconds):
        for _ in range(seconds):
            self.addOneSecond()

    def draw_clock(self,pen):
        pen.up()
        pen.goto(0, 210)
        pen.setheading(180)
        pen.color('green')
        pen.pendown()
        pen.circle(210)

        pen.penup()
        pen.goto(0,0)
        pen.setheading(90)

        for _ in range(12):
            pen.fd(190)
            pen.pendown()
            pen.fd(20)
            pen.penup()
            pen.goto(0,0)
            pen.rt(30)

        # hour hand
        pen.penup()
        pen.goto(0, 0)
        pen.color('orange')
        pen.setheading(90)
        angle = (self.hours/ 12) * 360
        pen.rt(angle)
        pen.pendown()
        pen.fd(100)

        # minute hand
        pen.penup()
        pen.goto(0, 0)
        pen.color('red')
        pen.setheading(90)
        angle = (self.minutes/ 60) * 360
        pen.rt(angle)
        pen.pendown()
        pen.fd(140)

        # second hand
        pen.penup()
        pen.goto(0, 0)
        pen.color('red')
        pen.setheading(90)
        angle = (self.seconds/ 60) * 360
        pen.rt(angle)
        pen.pendown()
        pen.fd(180)


turtle.listen()
