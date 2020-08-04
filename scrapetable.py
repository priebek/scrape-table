import requests
from bs4 import BeautifulSoup
import json

url = "http://www.slyngel.dk/handuo/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find('table', id='t01')

data = []

# https://www.codementor.io/@dankhan/web-scrapping-using-python-and-beautifulsoup-o3hxadit4
# http://tset.ninja/2018/12/02/2018-11-15-handuo-six-stars-movie-prediction/

# <tr>
all_tr = tb.find_all('tr')
for tr_item in all_tr[2:3]:

    # <td>
    all_td = tr_item.find_all('td')

    tmp = {}
    tmp['episode'] = all_td[0].a.text
    tmp['link'] = all_td[0].a.get('href')
    tmp['title'] = all_td[1].a.text
    tmp['imdb'] = all_td[1].a.get('href')
    tmp['type'] = all_td[2].text
    tmp['score'] = all_td[3].text
    tmp['category'] = all_td[4].text
    tmp['genre'] = all_td[5].text
    tmp['year'] = all_td[6].text
    tmp['broadcast'] = all_td[7].text

    data.append(tmp)

print(json.dumps(data))
