#
#
#

import requests

def DataPull():
    try:
        DataRaw = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
    except:
        print("Connection to the server could not be established.")

    BaseCurrSet = set()
    MarketCurrSet = set()

    for Shovel in DataRaw.json()["result"]:
        BaseCurrSet.add(Shovel["BaseCurrency"])
        MarketCurrSet.add(Shovel["MarketCurrency"])

    print(BaseCurrSet)
    print(MarketCurrSet)


if __name__ == '__main__':

    DataPull()
