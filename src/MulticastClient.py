import socket
import threading
import struct
from ServerEntry import *

MCAST_GRP = '228.1.1.1'
MCAST_PORT = 5007

class MulticastClient(threading.Thread):

    client = None
    servers = list()

    def __init__(self):
        threading.Thread.__init__(self)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client.bind((MCAST_GRP, MCAST_PORT))
        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
        self.client.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def run(self):
        while(True):
            #receiving the data 
            data,ip_adrr = self.client.recvfrom(1024)

            #adding server to list
            server = ServerEntry(ip_adrr[0], int(data))

            if server not in self.servers:
                self.servers.append(ServerEntry(ip_adrr[0], int(data)))
                self.servers.sort()
            elif server in self.servers:
                index = self.servers.index(server)
                self.servers[index].reset_timer()

            
            for s in self.servers:
                if s.timer_thread.remaining_time == 0:
                    self.deleteServer(s)

            print(self.servers)

    def deleteServer(self,server):
        self.servers.remove(server)

if __name__ == "__main__":
    obj = MulticastClient()
    obj.start()
    # servers = list()
    # ip = '192.168.1.1'

    # s1 = ServerID(ip,9000)
    # s2 = ServerID(ip,5000)
    # s3 = ServerID(ip,9005)
    # s4 = ServerID(ip,8300) 

    # servers.append(s1)
    # servers.append(s2)
    # servers.append(s3)
    # servers.append(s4)

    # servers.sort()

    # print(servers)