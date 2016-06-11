import time
from threading import Thread
from multiprocessing.pool import ThreadPool

distance = 0
def getDistance():

    print "in the thread"
    global distance
    while True:
        distance = distance+1
        print "distance from thread is %d" %(distance)
        time.sleep(.5)


    print "thread exiting"



def update():
    while True:
        time.sleep(.5)
        print "in main and distance is %d" % (distance)




thread = Thread(target= getDistance, args=())
thread.start()
update()
