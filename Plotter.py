# data_history = requests.get("https://bittrex.com/api/v1.1/public/getmarkethistory?market=" + base + "-" + market)
# for time in data_history["result"]["TimeStamp"]:
#   temp_data["TimeStamp"] = {}

import threading
import datamarket
import matplotlib.pyplot as plt



def refresh():

  threading.Timer(3.0, refresh).start()
  print("hi")
  ax.clear()
  datamarket.update_data("USDT", "ETH")
  x = datamarket.history[0]
  y = datamarket.history[1]
  ax.plot(x, y)
  plt.show()


datamarket.fetch_data("USDT", "ETH")
x = datamarket.history[0]
y = datamarket.history[1]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
refresh()
plt.show()

