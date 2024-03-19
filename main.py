from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from components.dataTableWidget import *
from components.fontComboBox import *
import fonts, assets
import sys

class Main(QWidget):
    def initFonts(self):
        for font in fonts.registered.keys():
            fontName = assets.find(f'./assets/SF-Pro-Display-{font}.otf')
            QFontDatabase.addApplicationFont(fontName)

    def __init__(self):
        super().__init__()
        self.initFonts()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SF Symbols')
        dataTableWidget = DataTableWidget()
        searchLineEdit = QLineEdit(self)
        searchLineEdit.setPlaceholderText('Search')
        searchLineEdit.textChanged.connect(dataTableWidget.findName)
        fontComboBox = FontComboBox(dataTableWidget)
        hbox = QHBoxLayout()
        hbox.addWidget(fontComboBox)
        hbox.addWidget(searchLineEdit)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(dataTableWidget)
        self.setWindowIcon(QIcon(assets.find('./assets/SFSymbolsIcon.ico')))
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 600)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont('SF Pro Display', 13))
    myWindow = Main()
    myWindow.show()
    app.exec_()