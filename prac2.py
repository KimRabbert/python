import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Festival_controller")
        self.setWindowIcon(QtGui.QIcon('inhun_favicon.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.resize(100, 100)
        btn.move(100, 100)
        btn.clicked.connect(self.close_application)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("1개")
        comboBox.addItem("2개")
        comboBox.addItem("3개")
        comboBox.addItem("4개")
        comboBox.addItem("5개")

        comboBox.activated[str].connect(self.choice)

        comboBox.move(200, 200)

        self.show()

    def choice(self):
        print("choice!!")

    def close_application(self):
        print("click!")




app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

