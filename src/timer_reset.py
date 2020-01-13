from TimerThread import *
import threading
import time

def reset_timer(t):
    time.sleep(5)
    t.remaining_time = 11

t = TimerThread()
t.start()

t1 = threading.Thread(target=reset_timer, args=(t,))
t1.start()