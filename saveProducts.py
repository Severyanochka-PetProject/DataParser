from asyncio.windows_events import NULL
import json
import requests

data = None

# with open('data.json', encoding='utf-8', newline='') as file:
#     data = json.load(file);

# for product in data:
#     # print(product);
#     res = requests.post('https://tankistpro-food.ru/product-apiV1/products/add-product', json=product)
#     print(res.text)


# Сохранение изображений продуктов

with open('images.json', encoding='utf-8', newline='') as file:
    data = json.load(file);

for link in data:
    print(link);
    res = requests.post('https://tankistpro-food.ru/fs-apiV1/save-product-image', headers = {
        'Content-Type': 'application/json',
    }, json={
        "img_link": link
    })

    print(res.text)