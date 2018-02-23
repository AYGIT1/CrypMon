# Ex. 2
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




class AppMain(QWidget):

    def data_pull():
        try:
            data_raw = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
        except:
            print("Connection to the server could not be established.")

        for Shovel in data_raw.json()["result"]:
            base_curr_set.add(Shovel["BaseCurrency"])
            market_curr_set.add(Shovel["MarketCurrency"])

    data_pull()

    def fetch_data(base, market):
        global history
        temp_data_time = []
        temp_data_price = []
        data_history = requests.get(
            "https://bittrex.com/api/v1.1/public/getmarkethistory?market=" + base + "-" + market)
        print(data_history.json()["result"])
        for time_price in data_history.json()["result"]:
            temp_data_time.append(time_price["TimeStamp"])  # TODO: convert to time
            temp_data_price.append(time_price["Price"])  # TODO: convert to float
        history = [temp_data_time, temp_data_price]

    def update_data(base, market):
        currency_rates = base + "-" + market
        currency_rates = currency_rates.upper()
        data_raw = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
        for data_market_sum in data_raw.json()["result"]:
            if data_market_sum['MarketName'] == currency_rates:
                history[0].insert(0, data_market_sum["TimeStamp"])
                history[1].insert(0, data_market_sum["Last"])
        return history

    def last_val_finder():
        values = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
        for data_Markets in values.json()["result"]:
            if data_Markets['MarketName'] == base + "-" + market:
                global last_val
                last_val = float(data_Markets["Last"])

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
        self.btn = QPushButton('Graph', self)
        # self.btn.clicked.connect(self.fetch_data( base, market))
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(40, 150)

        self.LastVal = QLabel(" ", self)
        self.LastVal.move(130, 160)
        self.LastVal.adjustSize()

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('CryptoCurrencyMonitor')
        self.show()

    def curr_change_name(self):
        # last_val_finder()
        global base, market
        base = self.BaseCombo.currentText()
        market = self.MarketCombo.currentText()
        # self.LastVal.setText("1 " + market + " = " + str(last_val) + " " + base)
        # self.LastVal.adjustSize()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppMain()
    sys.exit(app.exec_())
