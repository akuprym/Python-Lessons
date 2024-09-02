#  задание
#  1. Отправьте на https://api.binance.com/api/v3/ticker/price запрос БЕЗ аргумента params.
#  2. Изучите структуру ответа, сравните её с ответом в запросе без params.
#  3. Напишите код, который найдёт курс Etherium'а к доллару (ETHUSDT) в полученной из запроса структуре.

import requests

url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url)

for item in response.json():
    if item['symbol'] == "ETHUSDT":
        print(item['price'])









#  решение

import requests

response = requests.get('https://api.binance.com/api/v3/ticker/price')

for ticker in response.json():
    if ticker['symbol'] == 'ETHUSDT':
        pass
        # print(ticker['price'])
