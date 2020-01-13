from ServerID import *
from TimerThread import *
import threading

class ServerEntry(ServerID):
    
    def __init__(self, ip, port):
        super().__init__(ip, port)
        self.timer_thread = TimerThread(11,self)
        self.reset_timer()
        self.timer_thread.start()

    def reset_timer(self):
        self.timer_thread.remaining_time = 11




