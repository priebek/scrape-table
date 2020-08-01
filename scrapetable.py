import requests
from bs4 import BeautifulSoup
from itertools import islice

url = "http://www.slyngel.dk/handuo/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find('table', id='t01')

data = {}

# https://www.codementor.io/@dankhan/web-scrapping-using-python-and-beautifulsoup-o3hxadit4
# http://tset.ninja/2018/12/02/2018-11-15-handuo-six-stars-movie-prediction/

# test = tb.find_all('tr')
# next(test)
counter = 0

for link in tb.find_all('tr'):
    if counter == 30:
        break

    name = link.find('td')
    print(name)

    counter += 1
    # break;
    # print(name.get_text('href'))

