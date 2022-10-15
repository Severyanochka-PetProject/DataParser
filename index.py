from random import random
import json
import requests
import random
from bs4 import BeautifulSoup

url = "https://www.perekrestok.ru/cat/mc/113/moloko-syr-ajca"
response = requests.get(url = url)

soup = BeautifulSoup(response.text, 'html.parser')
products_list = soup.findAll('div', class_='sc-hYZPRl kxnVRY');

jsonList = [];
imagesList = [];

for product in products_list:
    product_img = product.find('img', class_='product-card__image')['data-src']
    product_name = product.find('div', class_='product-card__title').text
    product_price = str.replace(product.find('div', class_='price-new').text, ',', '.')[:-2]

    imagesList.append(product_img)
    
    product_payload = {
        "name": product_name,
        "description": "",
        "price": float(product_price),
        "url": "https://storage.yandexcloud.net/severyanochka-fs/products/" + product_img.split('/')[-1],
        "id_brand": random.randint(1, 10),
        "id_manufacture": random.randint(1, 7),
        "id_category": 6,
        "discount": 0,
    }

    jsonList.append(product_payload);

with open('images.json', 'w', encoding="utf-8") as outfile:
    json.dump(imagesList, outfile, ensure_ascii=False);

with open('data.json', 'w', encoding="utf-8") as outfile:
    json.dump(jsonList, outfile, ensure_ascii=False);
