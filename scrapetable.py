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

counter = -1

all_tr = tb.find_all('tr');
# print(t.counter);

for link in all_tr[2:10]:
    counter += 1

    print(link);
    # for l in link.find_all('td'):
    if counter == 10:
        break

        # name = link.find('td')
        # print(name.get_text('href'))

