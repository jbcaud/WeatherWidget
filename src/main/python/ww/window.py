# This Python file uses the following encoding: utf-8
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property
import datetime
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
        self.setContentsMargins(0,0,0,0)

        #set background image
        oImage = QPixmap.fromImage(self.ctx.back)
        sImage = oImage.scaled(QSize(self.width,self.height))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        #initialize layouts and labels
        citylayout = QHBoxLayout()
        self.futlayout = QHBoxLayout()
        windlayout = QVBoxLayout()
        self.labelname = QLabel()
        self.maintemp = QLabel()
        self.maintype = QLabel()

        #set fonts and colors of labels
        self.labelname.setFont(QFont('Lucida Handwriting', self.width/10 * 3/5))
        self.labelname.setStyleSheet("color: white;")
        self.maintemp.setFont(QFont('Lucida Handwriting', self.height/10 * 3/5))
        self.maintemp.setStyleSheet("color: white;")

        #set up the "city layout" (weather and pic)
        citylayout.addStretch(3)
        citylayout.addWidget(self.maintype)
        citylayout.addStretch()
        citylayout.addWidget(self.maintemp)
        citylayout.addStretch(3)

        #set up the window layout (everything)
        windlayout.addWidget(self.labelname)
        windlayout.setAlignment(self.labelname, Qt.AlignHCenter)
        windlayout.addLayout(citylayout)
        windlayout.addStretch(2)
        frame = QFrame()

        frame.setStyleSheet("background-color: black;")
        frame.setStyleSheet("background-color: rgba(0,0,0,160);")
        frame.setLayout(self.futlayout)
        frame.resize(500,500)
        windlayout.addWidget(frame)
        windlayout.addStretch(5)

        #get request from api
        request = requests.get("http://api.openweathermap.org/data/2.5/onecall?lat=33.300121&lon=-87.500282&APPID=c8acf3c2bf38a339b2495a3121255604&units=imperial")
        dictionary = request.json() #convert to dictionary

        #fill labels with information
        self.setMain(dictionary)
        self.setFuture(dictionary)


        #set layout
        windlayout.setContentsMargins(0,0,0,0)
        self.setLayout(windlayout)

    #sets the type of weather (image)
    def setType(self, ty, labeltype):
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
            labeltype.setPixmap(pixmap.scaled(ratiow , ratioh * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        elif (ty == "Clouds"):
            pixmap = self.ctx.cloudy
            labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        elif (ty == "Rain" or ty == "Drizzle"):
            pixmap = self.ctx.rainy
            labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        elif (ty == "Thunderstorm"):
            pixmap = self.ctx.thunderstorm
            labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        elif (ty == "Snow"):
            pixmap = self.ctx.snow
            labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        else:
            pixmap = self.ctx.other
            labeltype.setPixmap(pixmap.scaled(ratiow * 6/5, ratioh * 4.5/5, transformMode=QtCore.Qt.SmoothTransformation))

    #set up current forecast
    def setMain(self, dict):
        #store info in variables
        temp = str(math.floor(round(dict['current']['temp'])))
        name = "Tuscaloosa"
        type = dict['current']['weather'][0]['main']
        self.setType(type, self.maintype)

        #set name and temperature labels
        self.labelname.setText(name)
        self.maintemp.setText(temp+"°")

    def setDay(self, dict, num):
        #store info in variables
        temp = str(math.floor(round(dict['daily'][num]['temp']['day'])))
        type = dict['daily'][num]['weather'][0]['main']
        self.setType(type,self.currtype)
        if (type == "Clear"): self.currtype.setPixmap(self.ctx.sun.scaled(self.width / 10, self.height / 10 * 5.5/5, transformMode=QtCore.Qt.SmoothTransformation))
        #set name and temperature labels
        self.currtemp.setText(temp+"°")

    def setFuture(self, dict):
        for i in range(0, 6):
            currday = datetime.date.today() + datetime.timedelta(days = i + 1)
            forday = currday.strftime("%m/%d")
            daynum = QLabel()
            daynum.setText(forday)
            daylayout = QVBoxLayout()
            self.currtype = QLabel()
            self.currtemp = QLabel()
            daynum.setFont(QFont('Lucida Handwriting', self.height/10 * 2/5))
            daynum.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0);")
            self.currtemp.setFont(QFont('Lucida Handwriting', self.height/10 * 3/5))
            self.currtemp.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0);")
            self.currtype.setStyleSheet("background-color: rgba(255,255,255,0);")
            self.setDay(dict, i)
            daylayout.addWidget(daynum)
            daylayout.addWidget(self.currtype)
            daylayout.addWidget(self.currtemp)
            daylayout.setAlignment(daynum, Qt.AlignTop)
            daylayout.setAlignment(self.currtype, Qt.AlignCenter)
            self.futlayout.addLayout(daylayout)
            if i < 5: self.futlayout.addStretch(10);
