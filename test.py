from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import urllib3
import requests

from first import scrape


SearchTerm = "Mazda 3"
Location = "Canada"


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.kijiji.ca/')

browser.find_element_by_id('SearchKeyword').send_keys(SearchTerm)
browser.find_element_by_id('SearchLocationPicker').click()
browser.find_element_by_id('SearchLocationSelector-input').send_keys(Location)
time.sleep(1)
browser.find_element_by_id('SearchLocationSelector-input').send_keys(Keys.RETURN)
time.sleep(15)
searchResults = browser.current_url
#print(searchResults)

scrape(searchResults)

while(browser.find_element_by_xpath('//*[@title="Next"]') != 'None'):
    browser.find_element_by_xpath('//*[@title="Next"]').click()
    time.sleep(15)
    searchResults = browser.current_url
    scrape(searchResults)