import sys
from PySide6.QtWidgets import QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog

class Form(QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.edit = QLineEdit("Say something to the file!")
        self.button = QPushButton("Send to file!")
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        with open('dialog.txt','a') as file:
            file.write(f"{self.edit.text()}\n")

app = QApplication(sys.argv)
form= Form()
form.show()
sys.exit(app.exec())