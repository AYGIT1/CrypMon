#
#A little more than simple program to monitor cryptocurrency market values. Data pulled from bittrex.com
#
#

import sys
import requests
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QComboBox, QApplication)


BaseCurrSet = set()
MarketCurrSet = set()
#DataTup = ()
#TODO: Do not use global variables

def DataPull():
    try:
        DataRaw = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
    except:
        print("Connection to the server could not be established.")


    for Shovel in DataRaw.json()["result"]:
        BaseCurrSet.add(Shovel["BaseCurrency"])
        MarketCurrSet.add(Shovel["MarketCurrency"])

    # DataTup = BaseCurrSet, MarketCurrSet
    # print(DataTup)
    # for Code in DataTup[0]:
    #     print(type(Code))
    #     print(Code)

#def DataRefine():


class AppMain(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('QComboBox')
        self.show()

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



    #  def onActivated(self, text):
    #     self.BasLbl.setText(text)
    #     self.BasLbl.adjustSize()
    #     self.MarLbl.setText(text)
    #     self.MarLbl.adjustSize()


if __name__ == '__main__':
    DataPull()
    app = QApplication(sys.argv)
    ex = AppMain()
    sys.exit(app.exec_())