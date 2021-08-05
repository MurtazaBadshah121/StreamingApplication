from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("Python Streaming Application")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Login to the Streaming platform!")
        self.label.move(50,50)
        self.update()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Login")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button!")
        self.update()

    def update(self):
        self.label.adjustSize()



def clicked():
    print("success!!!")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()

