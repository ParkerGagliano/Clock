from Clock import Clock
import datetime


def main():
    now=datetime.datetime.now()
    c = Clock(now.hour, now.minute, now.second)
    c.start()

if __name__ == "__main__":
    main()



