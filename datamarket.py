import matplotlib.pyplot as plt
import requests
history = []


def fetch_data(base, market):
    global history
    temp_data_time = []
    temp_data_price = []
    data_history = requests.get("https://bittrex.com/api/v1.1/public/getmarkethistory?market="+base+"-"+market)
    for time_price in data_history.json()["result"]:
        temp_data_time.append(time_price["TimeStamp"]) #TODO: convert to time
        temp_data_price.append(time_price["Price"]) #TODO: convert to float
    history = [temp_data_time, temp_data_price]

def update_data(base, market):
    currency_rates = base+"-"+market
    currency_rates = currency_rates.upper()
    data_raw = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
    for data_market_sum in data_raw.json()["result"]:
        if data_market_sum['MarketName'] == currency_rates:
            history[0].insert(0, data_market_sum["TimeStamp"])
            history[1].insert(0, data_market_sum["Last"])
    return history


if __name__ == '__main__':
    fetch_data("USDT", "ETH")
    update_data("USDT", "ETH")
    print(history)
    plt.plot(history[0], history[1])
    plt.show()
