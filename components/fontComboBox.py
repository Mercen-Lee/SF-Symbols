from PySide6.QtWidgets import *
from PySide6.QtGui import *
import fonts

class FontComboBox(QComboBox):
    def __init__(self, tableWidget: QTableWidget):
        super().__init__()
        self.tableWidget = tableWidget
        self.initUI()
        
    def changeFont(self, value):
        for idx in range(self.tableWidget.rowCount()):
            symbolFont = QFont('SF Pro Display', 25)
            symbolWeight = QFont.Weight(fonts.registered[value])
            symbolFont.setWeight(symbolWeight)
            symbolItem = self.tableWidget.item(idx, 0)
            symbolItem.setFont(symbolFont)

    def initUI(self):
        self.addItems(fonts.registered)
        self.setCurrentIndex(5)
        self.currentTextChanged.connect(self.changeFont)