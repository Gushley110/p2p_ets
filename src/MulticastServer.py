import socket
import time
import threading

MCAST_GRP = '228.1.1.1'
MULTICAST_TTL = 5
MCAST_PORT = 5007

class MulticastServer(threading.Thread):
    
    server = None

    def __init__(self, msg):
        threading.Thread.__init__(self)
        
        self.msg = str(msg)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.server.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        
    def run(self):
        while True:
            try:
                #If socket is correctly initialized send message to group
                if self.server is not None:
                    self.server.sendto(self.msg.encode(), (MCAST_GRP, MCAST_PORT))
                    print('{} sent'.format(self.msg))
            except Exception as e:
                print('No se envio el mensaje')
                print(e)

            time.sleep(5)

if __name__ == "__main__":

    port = int(input("Puerto: "))
    obj = MulticastServer(port)

    obj.start()





# MCAST_GRP = '228.1.1.1'
# MCAST_PORT = 5007
# MCAST_MESSAGE = b'5000'
# # regarding socket.IP_MULTICAST_TTL
# # ---------------------------------
# # for all packets sent, after two hops on the network the packet will not 
# # be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
# MULTICAST_TTL = 2

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

# while True:

#     sock.sendto(MCAST_MESSAGE, (MCAST_GRP, MCAST_PORT))
#     time.sleep(5)