from bs4 import BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd



executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)

html = browser.html

soup = BeautifulSoup(html, 'html.parser')

results = soup.find('section', class_='image_and_description_container')
results = results.find('div', class_='content_title')
news_title = results.text
results = soup.find('section', class_='image_and_description_container')
results = results.find('div', class_='article_teaser_body')
news_p = results.text

browser.quit()


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://spaceimages-mars.com/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

results = soup.find('div', class_='header')
results = results.find('img', class_='headerimage')
featured_image_url = url + results['src']

browser.quit()

url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(url)
df = tables[0]


html_table = df.to_html()
html_table


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://marshemispheres.com/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

results = soup.find('div', class_='collapsible results')
results = results.find_all('div', class_='item')
hemisphere_images = []
hemisphere_image_urls = {}
for x in range(len(results)):
    link = results[x].find('div', class_='description')
    link = results[x].find('h3').text
    siteUrl = results[x].a['href']
    siteUrl = url + siteUrl
    browser.visit(siteUrl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find('div', class_='container')
    image = image.find('div', class_='wide-image-wrapper')
    image = image.find('img', class_='wide-image')
    image = url + image['src']
    hemisphere_image_urls['title' + ' ' + str(x)] = link
    hemisphere_image_urls['img_url'+ ' ' + str(x)] = image
hemisphere_images.append(hemisphere_image_urls)
# hemisphere_images

browser.quit()





