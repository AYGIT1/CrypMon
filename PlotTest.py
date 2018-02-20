import numpy as np
import matplotlib.pyplot as plt
import requests

data_Raw = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")

plt.axis([0, 18000, 0, 1])
plt.ion()

for i in range(10000):

    for data_Markets in data_Raw.json()["result"]:
        if data_Markets['MarketName'] == "USDT-BTC":
            y = int(data_Markets["Last"])
    plt.scatter(i, y)
    plt.pause(1)

while True:

    plt.pause(0.5)