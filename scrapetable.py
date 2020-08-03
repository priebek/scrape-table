import requests
from bs4 import BeautifulSoup

url = "http://www.slyngel.dk/handuo/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find('table', id='t01')

data = {}

# https://www.codementor.io/@dankhan/web-scrapping-using-python-and-beautifulsoup-o3hxadit4
# http://tset.ninja/2018/12/02/2018-11-15-handuo-six-stars-movie-prediction/

# <tr>
all_tr = tb.find_all('tr');
for tr_item in all_tr[2:3]:

    # <td>
    all_td = tr_item.find_all('td')
    print(all_td)
    for item in all_td:
    
        all_a = item.find_all('a');
        for a in all_a:
            print(a.get('href'));

        # print(item.get('href'));
        # print(item);

    counter += 1

    # print(link);
    # print(link.td.string);
    # print(link.a.string);

    # for l in link.find_all('td'):
    # if counter == 20:
    #     break

        # name = link.find('td')
        # print(name.get_text('href'))

