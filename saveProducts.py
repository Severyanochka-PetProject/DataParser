from asyncio.windows_events import NULL
import json
import requests

data = None

with open('data.json', encoding='utf-8', newline='') as file:
    data = json.load(file);

for product in data:
    # print(product);
    res = requests.post('https://tankistpro-food.ru/product-apiV1/products/add-product', json=product)
    print(res.text)

# file = open('data.json');
# data = json.load(file);

# print(file);

# file.close()