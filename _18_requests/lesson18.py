# in terminal: pip install requests

import requests
import time

url = 'https://api.binance.com/api/v3/ticker/price'

try:
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    content = response.content

    print(content)  # Output: b'{"symbol":"BTCUSDT","price":"57749.05000000"}'
    print(type(content))  # bytes

    price_object = response.json()
    price = float(price_object['price'])

    print(price)
    print(type(price))

except requests.exceptions.ConnectionError as error:
    print(f"Error occured: {error}")

"""
bitcoin_prices = []

for i in range(30):
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price_object = response.json()
    price = float(price_object['price'])
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))
"""