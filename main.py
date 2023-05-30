# import csv
# import requests
# from bs4 import BeautifulSoup

# url = 'http://link.kg/catalog/1/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# notebook_elements = soup.find_all('td', class_='tp')
# for x in notebook_elements:
#     print(x.text)

# price_dollars = notebook_elements.find('td', class_='tp').text
# print(price_dollars)

# print(notebook_elements)
# print(soup)

# data = []

# for notebook_element in notebook_elements:
#     td_elements = notebook_element.find_all('td')

#     if len(td_elements) >= 5:
#         notebook_title = td_elements[1].text.strip()
#         price_soms = td_elements[2].text.strip()
#         price_dollars = td_elements[3].text.strip()

#         data.append([notebook_title, price_soms, price_dollars])

# with open('notebooks.csv', mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Название ноутбука', 'Цена в сомах', 'Цена в долларах'])
#     writer.writerows(data)



import csv
import requests
from bs4 import BeautifulSoup

url = 'http://link.kg/catalog/1/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
notebook_elements = soup.find_all('tr', class_='r2')

data = []

for notebook_element in notebook_elements:
    td_elements = notebook_element.find_all('td')
    if len(td_elements) >= 5:
        notebook_title = td_elements[1].text.strip()
        price_soms = td_elements[2].text.strip()
        price_dollars = td_elements[3].text.strip()
        data.append([notebook_title, price_soms, price_dollars])

with open('notebooks.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Название ноутбука', 'Цена в сомах', 'Цена в долларах'])
    writer.writerows(data)
