import threading
import time 
from ServerEntry import *

class TimerThread(threading.Thread):

    def __init__(self,remaining_time=11,entry=None):
        threading.Thread.__init__(self)

        self.remaining_time = remaining_time
        self.entry = entry
        self.is_running = True

    def run(self):
        
        while True:
            time.sleep(1)
            self.remaining_time -= 1

            if self.remaining_time == 0:
                break

if __name__ == "__main__":
    pass

