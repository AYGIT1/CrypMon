#
#A little more than simple program to monitor cryptocurrency market values. Data pulled from bittrex.com
#
#

import sys
import requests
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QComboBox, QApplication)


BaseCurrSet = set()
MarketCurrSet = set()
#TODO: Do not use global variables

def data_pull():
    try:
        data_raw = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
    except:
        print("Connection to the server could not be established.")


    for Shovel in data_raw.json()["result"]:
        BaseCurrSet.add(Shovel["BaseCurrency"])
        MarketCurrSet.add(Shovel["MarketCurrency"])

def data_refine():

    #Base = Get string from self.BasLbl
    #Market = Get string from self.MarLbl
    #exchange = "Base" + "Market"

    try:
        data_marketsum = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
    except:
        print("Connection to the server could not be established.")

    for Bucket in data_marketsum.json()["result"]:
        if Bucket['MarketName'] == exchange:
            rates = [int(Bucket['High'), int(Bucket['Low']), int(Bucket['Last']),]
            
    return rates


class AppMain(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        ####### Base Currency Menu #######
        self.BasLbl = QLabel("Select a base currency", self)
        BaseCombo = QComboBox(self)
        BaseCombo.addItem("-")
        for Code in BaseCurrSet:
            BaseCombo.addItem(Code)
        self.BasLbl.move(35, 25)
        BaseCombo.move(35, 50)
        # BaseCombo.activated[str].connect(self.onActivated)

        ####### Market Currency Menu #######
        self.MarLbl = QLabel("Select a market currency", self)
        MarketCombo = QComboBox(self)
        MarketCombo.addItem("-")
        for Code in MarketCurrSet:            #TODO: Bad UX, should be in alphabetical order
            MarketCombo.addItem(Code)
        self.MarLbl.move(180, 25)
        MarketCombo.move(180, 50)
        # MarketCombo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    #  def onActivated(self, text):
    #     self.BasLbl.setText(text)
    #     self.BasLbl.adjustSize()
    #     self.MarLbl.setText(text)
    #     self.MarLbl.adjustSize()


if __name__ == '__main__':
    data_pull()
    app = QApplication(sys.argv)
    ex = AppMain()
    sys.exit(app.exec_())
