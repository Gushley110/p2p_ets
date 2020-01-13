# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.qlist_active_servers = QtWidgets.QListView(self.centralwidget)
        self.qlist_active_servers.setGeometry(QtCore.QRect(590, 40, 200, 300))
        self.qlist_active_servers.setObjectName("qlist_active_servers")
        self.qlbl_active_servers = QtWidgets.QLabel(self.centralwidget)
        self.qlbl_active_servers.setGeometry(QtCore.QRect(620, 10, 131, 20))
        self.qlbl_active_servers.setObjectName("qlbl_active_servers")
        self.qlog = QtWidgets.QTextBrowser(self.centralwidget)
        self.qlog.setGeometry(QtCore.QRect(20, 150, 281, 190))
        self.qlog.setObjectName("qlog")
        self.qlbl_msgs = QtWidgets.QLabel(self.centralwidget)
        self.qlbl_msgs.setGeometry(QtCore.QRect(30, 130, 58, 18))
        self.qlbl_msgs.setObjectName("qlbl_msgs")
        self.qin_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.qin_filename.setGeometry(QtCore.QRect(20, 40, 281, 32))
        self.qin_filename.setText("")
        self.qin_filename.setObjectName("qin_filename")
        self.qlbl_filename = QtWidgets.QLabel(self.centralwidget)
        self.qlbl_filename.setGeometry(QtCore.QRect(20, 10, 121, 18))
        self.qlbl_filename.setObjectName("qlbl_filename")
        self.qbtn_search = QtWidgets.QPushButton(self.centralwidget)
        self.qbtn_search.setGeometry(QtCore.QRect(20, 80, 88, 34))
        self.qbtn_search.setObjectName("qbtn_search")
        self.qlbl_next_node = QtWidgets.QLabel(self.centralwidget)
        self.qlbl_next_node.setGeometry(QtCore.QRect(650, 370, 101, 18))
        self.qlbl_next_node.setObjectName("qlbl_next_node")
        self.qlbl_prev_node = QtWidgets.QLabel(self.centralwidget)
        self.qlbl_prev_node.setGeometry(QtCore.QRect(80, 370, 91, 16))
        self.qlbl_prev_node.setObjectName("qlbl_prev_node")
        self.qlbl_prev_node_val = QtWidgets.QLabel(self.centralwidget)
        self.qlbl_prev_node_val.setGeometry(QtCore.QRect(80, 400, 58, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.qlbl_prev_node_val.setFont(font)
        self.qlbl_prev_node_val.setObjectName("qlbl_prev_node_val")
        self.qlbl_next_node_val = QtWidgets.QLabel(self.centralwidget)
        self.qlbl_next_node_val.setGeometry(QtCore.QRect(650, 400, 58, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.qlbl_next_node_val.setFont(font)
        self.qlbl_next_node_val.setObjectName("qlbl_next_node_val")
        self.qlist_filenames = QtWidgets.QListView(self.centralwidget)
        self.qlist_filenames.setGeometry(QtCore.QRect(365, 40, 200, 301))
        self.qlist_filenames.setObjectName("qlist_filenames")
        self.qlbl_filename_2 = QtWidgets.QLabel(self.centralwidget)
        self.qlbl_filename_2.setGeometry(QtCore.QRect(430, 10, 58, 18))
        self.qlbl_filename_2.setObjectName("qlbl_filename_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.qlbl_active_servers.setText(_translate("MainWindow", "Servidores Activos"))
        self.qlog.setPlaceholderText(_translate("MainWindow", "Log"))
        self.qlbl_msgs.setText(_translate("MainWindow", "Mensajes"))
        self.qin_filename.setPlaceholderText(_translate("MainWindow", "nombre_de_archivo.zip"))
        self.qlbl_filename.setText(_translate("MainWindow", "Nombre de archivo"))
        self.qbtn_search.setText(_translate("MainWindow", "Buscar"))
        self.qlbl_next_node.setText(_translate("MainWindow", "Nodo Siguiente"))
        self.qlbl_prev_node.setText(_translate("MainWindow", "Nodo Anterior"))
        self.qlbl_prev_node_val.setText(_translate("MainWindow", "s"))
        self.qlbl_next_node_val.setText(_translate("MainWindow", "t"))
        self.qlbl_filename_2.setText(_translate("MainWindow", "Archivos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
