#
# A little more than simple program to monitor cryptocurrency market values. Data pulled from bittrex.com
#
#

import sys
import requests
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication, QPushButton, QMessageBox)

base_curr_set = set()
market_curr_set = set()
base = "-"
market = "-"
last_val = 1.00000

# TODO: Do not use global variables

def data_pull():
    try:
        data_raw = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
    except:
        print("Connection to the server could not be established.")

    for Shovel in data_raw.json()["result"]:
        base_curr_set.add(Shovel["BaseCurrency"])
        market_curr_set.add(Shovel["MarketCurrency"])

def last_val_finder():
    values = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
    for data_Markets in values.json()["result"]:
        if data_Markets['MarketName'] == base + "-" + market:
            print("start")
            print(base + "-" + market)
            print(data_Markets["Last"])
            print("end")
            global last_val
            last_val = float(data_Markets["Last"])

class AppMain(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Base Currency Menu #######
        self.BasLbl = QLabel("Select a base currency", self)
        self.BaseCombo = QComboBox(self)
        self.BaseCombo.addItem("-")
        for Code in base_curr_set:
            self.BaseCombo.addItem(Code)
        self.BasLbl.move(40, 25)
        self.BaseCombo.move(40, 50)
        self.BaseCombo.currentTextChanged.connect(self.curr_change_name)

        # Market Currency Menu #######
        self.MarLbl = QLabel("Select a market currency", self)
        self.MarketCombo = QComboBox(self)
        self.MarketCombo.addItem("-")
        for Code in market_curr_set:  # TODO: Bad UX, should be in alphabetical order
            self.MarketCombo.addItem(Code)
        self.MarLbl.move(180, 25)
        self.MarketCombo.move(180, 50)
        self.MarketCombo.currentTextChanged.connect(self.curr_change_name)

        # Button #
        self.btn = QPushButton('Button', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(40, 150)

        self.LastVal = QLabel(" ",self)
        self.LastVal.move(130, 160)
        self.LastVal.adjustSize()

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    def curr_change_name(self):
        last_val_finder()
        global base, market
        base = self.BaseCombo.currentText()
        market = self.MarketCombo.currentText()
        self.LastVal.setText("1 " + market + " = " + str(last_val) + " " + base)
        self.LastVal.adjustSize()

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

