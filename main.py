from PyQt5.QtWidgtets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, BasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
import sys, random


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        '''initiates application UI'''

        self.tboard = Board(self)        # Board is a class that follows after this class
        self.SetCentralWidget(self.tboard       # This adds the Board to the Qt central widget

        self.statusbar = self.statusBar()       # This is the Qt status bar (build)
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)     # This is showing the score and game over

        self.tboard.start()      #This will start the game off

        self.resize(180, 380)    #Size of the window
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        '''centers the window on the screen'''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)