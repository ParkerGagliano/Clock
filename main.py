from Clock import Clock
import time
import threading





currentTime = time.ctime(time.time())[-14:-5]
def convertTime(a):
    hours=int(a[0:3])
    minutes=int(a[4:6])
    seconds=int(a[7:9])
    return[hours, minutes, seconds]

converted = convertTime(currentTime)
c = Clock(converted[0], converted[1], converted[2])
clock_thread = threading.Thread(target=c.start)
clock_thread.start()
time.sleep(5)
c.pause()
c.addTime(10)

