#PyQt5 Basics
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QCheckBox, QComboBox, QProgressBar, QStyleFactory, QLineEdit, QInputDialog, QMainWindow, QAction, qApp, QTextEdit, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import sys 
import time 
#create a class that inherits from QMainWindow
#create a window with basic button and connected function 
class MyWindow(QMainWindow):

    def __init__(self):
        #call parent constructor 
        super(MyWindow, self).__init__()
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Flos Test Window")
        self.initUI()
    
    def initUI(self):
        #Labels (displays text )
        self.label = QtWidgets.QLabel(self)
        self.label.setText("thats a label1")
        self.label.move(50,50)

        #Buttons and Button Presses
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("click me")
        self.button1.clicked.connect(self.buttonfunction)

    def buttonfunction(self):
        self.label.setText("you pressed the button")
        
        
        self.update()
    #update the size of the widget t fit in the content
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()




