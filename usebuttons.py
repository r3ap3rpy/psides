import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

@Slot()
def welcome():
    print("Print the stufff of legends!")

app = QApplication(sys.argv)
button = QPushButton("Click meeee!")
button.clicked.connect(welcome)
button.show()
sys.exit(app.exec())