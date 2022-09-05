from Clock import Clock
import datetime
import turtle


def main():
    wn=turtle.Screen()
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.title("Analog clock")
    wn.tracer(0)
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    now=datetime.datetime.now()
    c = Clock(now.hour, now.minute, now.second, pen, wn)
    c.start()

if __name__ == "__main__":
    main()



