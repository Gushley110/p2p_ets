from main_ui import *
from MulticastServer import *
from MulticastClient import *
import sys

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self, port):
        QtWidgets.QMainWindow.__init__(self)
        self.port = port
        self.servers = list()

        self.prevNode = None
        self.nextNode = None

        # create UI
        self.setupUi(self)
        self.setWindowTitle(str(self.port))

        self.qlbl_prev_node_val.setText('')
        self.qlbl_next_node_val.setText('')

        self.qbtn_search.clicked.connect(self.update)

        # init multicast server
        self.mcast_server = MulticastServer(self.port)
        self.mcast_server.start()
        self.qlog.append('Iniciando nodo en puerto {}'.format(self.port))
        # init multicast client
        self.mcast_client = MulticastClient()
        self.mcast_client.start()
        self.servers = self.mcast_client.servers
        

        # Call function update every 5 seconds
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(5000)

        self.entry = QtGui.QStandardItemModel()
        self.qlist_active_servers.setModel(self.entry)


    
    def contextMenuEvent(self, event):
        print("Context menu event!")

    def update(self):
        # Update Servers
        self.updateServersList()

        # Update previous and next
        self.updatePrevNextNodes()
        

    def updateServersList(self):
        # Clears list
        self.entry.clear()
        
        # Refills list with current servers
        for s in self.servers:
            it = QtGui.QStandardItem(str(s))
            self.entry.appendRow(it)

    def updatePrevNextNodes(self):
        size = len(self.servers)
        if size != 0:
            ip = self.servers[0].ip

            tempServerID = ServerID(ip,self.port)
            tempPrevNode = self.prevNode
            tempNextNode = self.nextNode
            try:
                index = self.servers.index(tempServerID)
                del(tempServerID)
                
                self.prevNode = self.servers[(index - 1) % size ]
                self.nextNode = self.servers[(index + 1) % size ]

                if self.prevNode != tempPrevNode:
                    self.qlog.append('Nodo anterior ha cambiado')

                if self.nextNode != tempNextNode:
                    self.qlog.append('Nodo siguiente ha cambiado')

                self.qlbl_prev_node_val.setText(str(self.prevNode))
                self.qlbl_prev_node_val.adjustSize()
                self.qlbl_next_node_val.setText(str(self.nextNode))
                self.qlbl_next_node_val.adjustSize()
            except Exception as e:
                print(e)
            
    
    
            

    


if __name__ == "__main__":
    port = int(input("Puerto:"))

    app = QtWidgets.QApplication([])
    window = MainWindow(port)
    window.show()
    app.exec_()