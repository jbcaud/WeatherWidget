# This Python file uses the following encoding: utf-8
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property
import requests
import math

class window(QWidget):

    def __init__(self, ctx):
        QWidget.__init__(self)
        self.ctx = ctx
        #set width and height of window
        self.width = 500
        self.height = 400
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        #set background image
        oImage = QPixmap.fromImage(self.ctx.back)
        sImage = oImage.scaled(QSize(self.width,self.height))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        #self.setStyleSheet("background-color: #3E5BFA;")

        #initialize layouts and labels
        citylayout = QHBoxLayout()
        windlayout = QVBoxLayout()
        self.labelname = QLabel()
        self.labeltemp = QLabel()
        self.labeltype = QLabel()

        #set fonts and colors of labels
        self.labelname.setFont(QFont('Lucida Handwriting', self.width/10 * 3/5))
        self.labelname.setStyleSheet("color: white;")
        self.labeltemp.setFont(QFont('Lucida Handwriting', self.height/10 * 3/5))
        self.labeltemp.setStyleSheet("color: white;")

        #set up the "city layout" (weather and pic)
        citylayout.addStretch(3)
        citylayout.addWidget(self.labeltype)
        citylayout.addStretch()
        citylayout.addWidget(self.labeltemp)
        citylayout.addStretch(3)

        #set up the window layout (everything)
        windlayout.addWidget(self.labelname)
        windlayout.setAlignment(self.labelname, Qt.AlignHCenter)
        windlayout.addLayout(citylayout)
        windlayout.addStretch()

        #fill labels with information
        self.getInfo()

        #set layout
        self.setLayout(windlayout)

    #executes when window set up
    def getInfo(self):
        #get request from api
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Tuscaloosa,al,us&APPID=c8acf3c2bf38a339b2495a3121255604&units=imperial")
        dict = r.json() #convert to dictionary

        #store info in variables
        temp = str(math.floor(round(dict['main']['temp'])))
        name = dict['name']
        ty = dict['weather'][0]['main']

        #set picture and size of type label
        ratiow = self.width / 10
        ratioh = self.height / 10
        if (ty == "Clear"):
            time = QTime()
            #if it is after 6 PM, have moon pic
            if (time.currentTime().hour() > 18):
                pixmap = self.ctx.moon
            else: #otherwise use sun pic
                pixmap = self.ctx.sun
            self.labeltype.setPixmap(pixmap.scaled(ratiow, ratioh, transformMode=QtCore.Qt.SmoothTransformation))
        elif (ty == "Clouds"):
            pixmap = self.ctx.cloudy
            self.labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 4.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        elif (ty == "Rain" or ty == "Drizzle"):
            pixmap = self.ctx.rainy
            self.labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        elif (ty == "Thunderstorm"):
            pixmap = self.ctx.thunderstorm
            self.labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        elif (ty == "Snow"):
            pixmap = self.ctx.snow
            self.labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        else:
            pixmap = self.ctx.other
            self.labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 4.5/5, transformMode=QtCore.Qt.SmoothTransformation))

        #set name and temperature labels
        self.labelname.setText(name)
        self.labeltemp.setText(temp+"°")


