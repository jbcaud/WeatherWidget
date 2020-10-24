import sys
from PyQt5.QtWidgets import QApplication
from window import window

if __name__ == "__main__":
    app = QApplication([])
    window = window()
    window.show()
    sys.exit(app.exec_())
