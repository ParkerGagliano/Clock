from Clock import Clock
import datetime


now=datetime.datetime.now()

c = Clock(now.hour, now.minute, now.second)
c.start()


