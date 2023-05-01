import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets , QtCore , QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QMainWindow ,QDesktopWidget ,QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
import resources
import test

global dire

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("Main.ui",self)
        self.pushButton.clicked.connect(self.browse)
        self.pushButton_2.clicked.connect(self.gotoscreen2)
        self.pushButton_5.clicked.connect(self.gotoquit)
        self.pushButton_3.clicked.connect(self.call_function1)
        self.pushButton_4.clicked.connect(self.call_function2)

    
    def call_function1(self):
        try:
            test.test_Detection(dire)
        except:
            print("Specified path not found!:(\n")
    
    def call_function2(self):
        try:
            test.test_Detection_camera()
        except:
            print("Camera Not Found!:(\n")
            

    def browse(self):
        file_filter = 'Data File (*.mp4 *.avi *.3gp);; Media File (*.mp4 *.avi *.3gp)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
  
        )
        global dire
        dire = response[0]

    def gotoscreen2(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoquit(self):
        quit()

class Screen2(QMainWindow):
    def __init__(self):
        super(Screen2,self).__init__()
        loadUi("About.ui",self)
        
        
        self.pushButton.clicked.connect(self.gotopreviousscreen)
        self.pushButton_5.clicked.connect(self.gotoquit)

    def gotopreviousscreen(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    def gotoquit(self):
        quit()



app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()

mainwindow=MainWindow()
screen2=Screen2()

widget.addWidget(mainwindow)
widget.addWidget(screen2)
widget.setFixedHeight(571)
widget.setFixedWidth(1021)
widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)



widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")

