import time
import json
import requests
import binance
#from binance.client import Client
import bybit
from config import config
# 각 거래소 가격 가져오는 class
class prices:
    def __init__(self) -> None:
        conf = config()
        self.dydx_api_key = conf.conf["apis"]["dydx_api"]["api_key"]
        self.dydx_secret_key = conf.conf["apis"]["dydx_api"]["secret_key"]
        self.bybit_api_key = conf.conf["apis"]["bybit_api"]["api_key"]
        self.bybit_secret_key = conf.conf["apis"]["bybit_api"]["secret_key"]

    def dydx(self):
        #dydx 거래소 가격 및 호가창 가져오기
        response = requests.get('https://api.dydx.exchange/v1/ticker', params={
            'market': 'SOL-USD',
        }, headers={
            'Authorization': self.dydx_api_key,
            'DYDX-SIGNATURE': self.dydx_secret_key,
        })

        if response.status_code == 200:
            data = json.loads(response.text)
            print('SOL current price:', data['price'])
        else:
            print('Error:', response.status_code)
        ticker = b_client.get_ticker(symbol='SOLUSDT')

        return ticker['lastPrice']

    def bybit():
        #bybit 거래소 가격 및 호가창 가져오기
        client = bybit.bybit(test=False, api_key="", api_secret="")
        symbol = "SOLUSD"
        subscribe_orderbook = {"op": "subscribe", "args": [f"{symbol}.OrderBook_200"]}
        subscribe_trade = {"op": "subscribe", "args": [f"{symbol}.Trade"]}

price = prices()
print(price.dydx_api_key)