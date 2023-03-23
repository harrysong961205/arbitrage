import time
import json
from binance.client import Client

#바이낸스
b_api_key = 'your_api_key'
b_api_secret = 'your_api_secret'

b_client = Client(b_api_key, b_api_secret)

 


dydx_api_key = 'your_api_key'
dydx_secret_key = 'your_secret_key'

while True:
    response = requests.get('https://api.dydx.exchange/v1/ticker', params={
        'market': 'SOL-USD',
    }, headers={
        'Authorization': dydx_api_key,
        'DYDX-SIGNATURE': dydx_secret_key,
    })

    if response.status_code == 200:
        data = json.loads(response.text)
        print('SOL current price:', data['price'])
    else:
        print('Error:', response.status_code)
    ticker = b_client.get_ticker(symbol='SOLUSDT')
    print('SOL current price: ', ticker['lastPrice'])
    time.sleep(5) 

