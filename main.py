from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

stylesheet = """
    MainWindow {
        background-image: url("resources/images/bg.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    app.setStyleSheet(stylesheet) 
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())