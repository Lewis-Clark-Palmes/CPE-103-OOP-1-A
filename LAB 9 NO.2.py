import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()#initialize the main window like in the previous one
        #window = QMainWindow()
        self.title= "X"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200,200,300,300)
        self.setWindowIcon(QIcon('twitter_x_new_logo_x_icon_256077.ico')) #set an icon
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())