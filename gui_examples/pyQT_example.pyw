import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def PyQT5App():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(500, 500, 1000, 500)
    b.move(450, 240)
    w.setWindowTitle("PyQt5")
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    PyQT5App()
