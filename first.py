
print ("Start")

from bs4 import BeautifulSoup
import urllib3
import requests


def delNewLine(word):
    word = word.replace('\r', '').replace('\n', '')
    return word

def scrape(URL):
    #http = urllib3.PoolManager()
    #print(URL)
    #URL = 'https://www.kijiji.ca/b-canada/mazda-3/k0l0?rb=true&dc=true'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    #r = http.request('GET', 'https://www.kijiji.ca/b-canada/mazda-3/k0l0?rb=true&dc=true')

    search = soup.find_all(class_='search-item')
    #print (r.status)
    #print (search[0])

    j = 0

    for i in search:
        title = i.find(class_='title')
        price = i.find(class_='price')
        pic = i.find(class_='image')
        pic = pic.find('img')
        link = title.find('a')
        titletxt = title.get_text()
        pricetxt = price.get_text()
        titletxt = delNewLine(titletxt)
        pricetxt = delNewLine(pricetxt)

        print(titletxt)
        print(pricetxt)
        #if(pic['data-src'] != 'None'):
        print(pic.get('data-src', {'data-src':True}))
        
        print(link['href'])

