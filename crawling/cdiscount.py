from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Variable
url = 'http://www.cdiscount.com/search/10/{}+ordinateur+portable.html?&page={}#_his_'
types = ['DELL', 'ACER']
old_price = []
new_price = []
brand = []
discount = []
dic = {'brand': brand, 'old_price': old_price, 'new_price': new_price, 'discount': discount}
average_discount = {'dell': 0, 'acer': 0}
nb_pages = 2

for t in types:
    for page in range(1, nb_pages):
        response = requests.get(url.format(t, str(page)))
        soup = BeautifulSoup(response.text, 'html.parser')
        devices = soup.select("#lpBloc > li")
        for device in devices:
            if device.select(".prdtPrSt") != [] and device.select(".prdtPrSt")[0].text != '':
                brand.append(t)
                old_price.append(float(device.select(".prdtPrSt")[0].text.replace(',', '.')))
                new_price.append(float(device.select(".price")[0].text.replace('€', '.').replace(' ', '')))
                discount.append(float(((old_price[-1] - new_price[-1]) / old_price[-1]) * 100))

df = pd.DataFrame(dic)
df.to_csv('cdiscount_dell_acer.csv', encoding='utf-8')
print('*********************{}*************************'.format('DELL'))
print('\t\tAverage discount: ' + str(round(np.mean(df[df['brand'] == 'DELL']['discount']), 2)) + '%')
print()
print('*********************{}*************************'.format('ACER'))
print('\t\tAverage discount: ' + str(round(np.mean(df[df['brand'] == 'ACER']['discount']), 2)) + '%')
df