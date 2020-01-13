

class ServerID:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __hash__(self):
        return hash(ip+str(port))

    def __eq__(self, other):
        return other.ip + str(other.port) == self.ip + str(self.port)

    def __lt__(self, other):
        return self.port < other.port

    def ___gt__(self,other):
        return self.port > other.port

    def __str__(self):
        return self.ip + ':' + str(self.port)

    def __repr__(self):
        return self.ip + ':' + str(self.port)