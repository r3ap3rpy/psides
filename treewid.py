import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

data = {
    "Demo Project" : ["test.py","main.py","__init__.py"],
    "Another Project" : ["main.py"],
    "Abandoned Project" : []
}

app = QApplication()
tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Project","Workers"])

items = []
for key, values in data.items():
    item = QTreeWidgetItem([key])
    for value in values:
        ext = value.split('.')[-1].upper()
        child = QTreeWidgetItem([value, ext])
        item.addChild(child)
    items.append(item)
tree.insertTopLevelItems(0,items)

tree.show()
sys.exit(app.exec())