# This Python file uses the following encoding: utf-8
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import requests
import math

class window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setStyleSheet("background-color: #3E5BFA;")
        #initialize button, layout, and label
        button = QPushButton('Click for updates!', self)
        citylayout = QHBoxLayout()
        windlayout = QVBoxLayout()
        self.labelname = QLabel()
        self.labeltemp = QLabel()
        self.labeltype = QLabel()

        #set where and size of label/button
        self.labelname.setFont(QFont('Arial', 36))
        self.labelname.setStyleSheet("color: white;")
        self.labeltemp.setFont(QFont('Arial', 36))
        self.labeltemp.setStyleSheet("color: white;")
        #self.labeltype.setFont(QFont('Arial', 24))
        #self.labeltype.setStyleSheet("color: white;")

        #add button and label to the layout
        citylayout.addWidget(self.labelname)
        citylayout.addStretch(5)
        citylayout.addWidget(self.labeltype)
        citylayout.addStretch(1)
        citylayout.addWidget(self.labeltemp)
        windlayout.addLayout(citylayout)
        windlayout.addStretch()
        windlayout.addWidget(button)


        #set label at first, button executes and updates when clicked
        self.getInfo()
        button.clicked.connect(self.getInfo)

        #set layout
        self.setLayout(windlayout)

    #executes when button clicked
    def getInfo(self):
        #get request from api
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Tuscaloosa,al,us&APPID=c8acf3c2bf38a339b2495a3121255604&units=imperial")
        dict = r.json() #convert to dictionary

        #store info in variables and then fill label
        temp = str(math.floor(round(dict['main']['temp'])))
        name = dict['name']
        ty = dict['weather'][0]['main']
        if (ty == "Clear"):
            pixmap = QPixmap('img/moon.png')
            self.labeltype.setPixmap(pixmap.scaled(50, 50, transformMode=QtCore.Qt.SmoothTransformation))
            self.labeltype.resize(50,50)
        self.labelname.setText(name)
        self.labeltemp.setText(temp+"°")
        #self.labeltype.setText(ty)

