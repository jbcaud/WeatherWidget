# This Python file uses the following encoding: utf-8

from PyQt5.QtWidgets import QWidget, QPushButton

class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        button = QPushButton('Click for updates!', self)
        button.clicked.connect(self.clickMethod)
        button.resize(132, 50)
        button.move(50,50)

    def clickMethod(self):
        print('Hello World!')


