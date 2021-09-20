import requests
from bs4 import BeautifulSoup
import pandas as pd


data = {'name': [],
        'symbol': [],
        'price': [],
        'link': [],
        }

URL = "https://coinmarketcap.com/"

page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

rows = soup.find_all('tr', attrs={'class': 'sc-1rqmhtg-0'})

for row in rows:
    spans = (row.find_all('span'))
    price = 0
    span_item = 0
    name = ""
    for item in spans:
        span_item += 1
        if span_item == 4:
            name = item.text
        if "$" in item:
            price = item
    symbol = (row.find('span', attrs={'class': 'crypto-symbol'}))
    data["name"].append(name)
    data["symbol"].append(symbol.text)
    data["price"].append(price.text)
    data["link"].append("https://coinmarketcap.com" + row.a["href"])
csv_export = (pd.DataFrame.from_dict(data))
csv_export.to_csv("coinmarketcap_export.csv")
