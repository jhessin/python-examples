import sys
from PySide.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QLabel,
                              QVBoxLayout, QWidget)
from __feature__ import snake_case, true_property


class PySideApp(QWidget):
   def __init__(self):
       QWidget.__init__(self)

       self.message = QLabel("Hello PySide World!")
       self.message.alignment = Qt.AlignCenter

       self.layout = QVBoxLayout(self)
       self.layout.add_widget(self.message)


if __name__ == "__main__":
   app = QApplication(sys.argv)

   widget = PySideApp()
   widget.show()

   sys.exit(app.exec())
