#
#A little more than simple program to monitor cryptocurrency market values. Data pulled from bittrex.com
#
#

import sys
import requests
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)


BaseCurrSet = set()
MarketCurrSet = set()

def DataPull():
    try:
        DataRaw = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
    except:
        print("Connection to the server could not be established.")



    for Shovel in DataRaw.json()["result"]:
        BaseCurrSet.add(Shovel["BaseCurrency"])
        MarketCurrSet.add(Shovel["MarketCurrency"])

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

    ####### Base Currency Menu #######
        self.BasLbl = QLabel("Select a base currency", self)
        BaseCombo = QComboBox(self)
        BaseCombo.addItem("Ubuntsdgu")
        BaseCombo.addItem("Mandriva")
        self.BasLbl.move(35, 25)
        BaseCombo.move(35, 50)
        BaseCombo.activated[str].connect(self.onActivated)

    ####### Market Currency Menu #######
        self.MarLbl = QLabel("Select a market currency", self)
        MarketCombo = QComboBox(self)
        MarketCombo.addItem("Osman ")
        MarketCombo.addItem("Hayri")
        self.MarLbl.move(150, 25)
        MarketCombo.move(150, 50)
        MarketCombo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.BasLbl.setText(text)
        self.BasLbl.adjustSize()
        self.MarLbl.setText(text)
        self.MarLbl.adjustSize()


if __name__ == '__main__':
    DataPull()
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
