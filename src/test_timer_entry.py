from ServerEntry import *
import time 

servers = list()

ip = '192.168.1.1'

s1 = ServerEntry(ip,9000)

time.sleep(5)

s2 = ServerEntry(ip,9002)
s3 = ServerEntry(ip,9003)
s4 = ServerEntry(ip,9004)
s5 = ServerEntry(ip,9005)

while True:
    print('s1: {}'.format(s1.timer_thread.remaining_time))
    print('s2: {}'.format(s2.timer_thread.remaining_time))
    time.sleep(3)
