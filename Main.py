#
# A little more than simple program to monitor cryptocurrency market values. Data pulled from bittrex.com
#
#

import sys
import requests
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication, QPushButton, QMessageBox)

BaseCurrSet = set()
MarketCurrSet = set()
# TODO: Do not use global variables

def data_pull():
    try:
        data_raw = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
    except:
        print("Connection to the server could not be established.")

    for Shovel in data_raw.json()["result"]:
        BaseCurrSet.add(Shovel["BaseCurrency"])
        MarketCurrSet.add(Shovel["MarketCurrency"])


class AppMain(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Base Currency Menu #######
        self.BasLbl = QLabel("Select a base currency", self)
        self.BaseCombo = QComboBox(self)
        self.BaseCombo.addItem("-")
        for Code in BaseCurrSet:
            self.BaseCombo.addItem(Code)
        self.BasLbl.move(40, 25)
        self.BaseCombo.move(40, 50)
        self.BaseCombo.currentTextChanged.connect(self.base_change_name)

        # Market Currency Menu #######
        self.MarLbl = QLabel("Select a market currency", self)
        self.MarketCombo = QComboBox(self)
        self.MarketCombo.addItem("-")
        for Code in MarketCurrSet:  # TODO: Bad UX, should be in alphabetical order
            self.MarketCombo.addItem(Code)
        self.MarLbl.move(180, 25)
        self.MarketCombo.move(180, 50)
        self.MarketCombo.currentTextChanged.connect(self.market_change_name)

        # self.btn = QPushButton('Button', self)
        # self.btn.resize(self.btn.sizeHint())
        # self.btn.move(40, 150)
        #
        # self.LastVal = QLabel("Last Value: " ,self)
        # self.LastVal.move(130, 160)
        # self.LastVal.adjustSize()

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    def base_change_name(self):


    def market_change_name(self):


    # def closeEvent(self, event):
    #
    #     reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


if __name__ == '__main__':
    data_pull()
    app = QApplication(sys.argv)
    ex = AppMain()
    sys.exit(app.exec_())

