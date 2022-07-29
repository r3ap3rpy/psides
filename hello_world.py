import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
#lablel = QLabel("Hello World!")
lablel = QLabel("<font color=red size = 40>Hello World!</font>")
lablel.show()
sys.exit(app.exec())