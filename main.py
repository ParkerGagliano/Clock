from os import lseek
from Clock import Clock
import time
import threading
import turtle
import datetime


now=datetime.datetime.now()
wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analog clock")

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

c = Clock(now.hour, now.minute, now.second)
clock_thread = threading.Thread(target=c.start)
clock_thread.start()
time.sleep(5)
c.pause()
c.addTime(10)

def draw_clock(pen):
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
    angle = (c.hours/ 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('red')
    pen.setheading(90)
    angle = (c.minutes/ 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(140)

    # second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('red')
    pen.setheading(90)
    angle = (c.seconds/ 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

draw_clock(pen)
wn.mainloop()
