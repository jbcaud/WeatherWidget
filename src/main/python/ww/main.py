from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property
from PyQt5.QtWidgets import QMainWindow

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
from window import window

class AppContext(ApplicationContext):
    def run(self):
        self.main_window.show()
        return self.app.exec_()

    @cached_property
    def moon(self):
        return QPixmap(self.get_resource("images/moon.png"))

    @cached_property
    def sun(self):
        return QPixmap(self.get_resource("images/sun.png"))

    @cached_property
    def cloudy(self):
        return QPixmap(self.get_resource("images/cloudy.png"))

    @cached_property
    def rainy(self):
        return QPixmap(self.get_resource("images/rainy.png"))

    @cached_property
    def thunderstorm(self):
        return QPixmap(self.get_resource("images/thunderstorm.png"))

    @cached_property
    def snow(self):
        return QPixmap(self.get_resource("images/snow.png"))

    @cached_property
    def other(self):
        return QPixmap(self.get_resource("images/other.png"))

    @cached_property
    def back(self):
        return QImage(self.get_resource("images/back1.jpg"))


if __name__ == '__main__':
    app = QApplication([])
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    window = window(appctxt)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)



