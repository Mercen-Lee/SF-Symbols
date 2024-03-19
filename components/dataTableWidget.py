from PySide6.QtWidgets import *
from PySide6.QtGui import *
import assets
import json

class DataTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def findName(self, value):
        searchText = value.lower()
        for row in range(self.rowCount()):
            item = self.item(row, 1)
            self.setRowHidden(row, searchText not in item.text().lower())

    def initUI(self):
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setColumnCount(2)
        self.setColumnWidth(0, 70)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(50)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        with open(assets.find('./assets/SFSymbols.json'), 'r', encoding = 'UTF8') as data:
            sfsymbols = json.load(data)
            self.setRowCount(len(sfsymbols))
            for idx, symbol in enumerate(sfsymbols):
                symbolItem = QTableWidgetItem(symbol['symbol'])
                symbolFont = QFont('SF Pro Display', 25)
                symbolFont.setWeight(QFont.Weight(400))
                symbolItem.setFont(symbolFont)
                symbolItem.setTextAlignment(Qt.AlignCenter)
                self.setItem(idx, 0, symbolItem)
                self.setItem(idx, 1, QTableWidgetItem(symbol['name']))
        return self