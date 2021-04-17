#!/usr/bin/env python
# coding: utf-8

#import dependencies

import pandas as pd
import pymongo
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, redirect, render_template
from flask_pymongo import PyMongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

def scrape():
# Step 1 - Scraping

# ### NASA Mars News
# Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.


# Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

# URLs of pages to be scraped
    url = 'https://redplanetscience.com/'

    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')

#Scrap site to collect news title 
    news_title=soup.find_all('div', class_='content_title')[0].text

#Scrap site to collect paragraph text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text


# ### Featured Image
# Visit the url for the Featured Space Image.
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
# Make sure to find the image url to the full size `.jpg` image.
# Make sure to save a complete url string for this image.



#Set up splinter path for image
    img_url = 'https://spaceimages-mars.com'

#connect to site to begin scraping
    browser.visit(img_url)
    html=browser.html
    img_soup=bs(html,'html.parser')

#scrape image
    featured_image_url=img_soup.find('div', class_='header')

    featured_image_url=featured_image_url.find('img', class_='headerimage fade-in')

    src = featured_image_url

    full_url = img_url+'/'+src['src']



# ### Mars Facts 
# Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.

# set url for fact scraping
    facts_url = 'https://galaxyfacts-mars.com'

    tables = pd.read_html(facts_url)

# separate each table to a df and turn into HTML script
    df=pd.DataFrame(tables[0])

    df2=pd.DataFrame(tables[1])

    html_facts=df.to_html()

    html_facts2=df2.to_html()



# Mars Hemispheres
# Visit the astrogeology site to obtain high resolution images for each of Mar's hemispheres.


# set image url
    hemi_url = 'https://marshemispheres.com/'

# connect to site to begin scraping
    browser.visit(hemi_url)
    html=browser.html
    hemi_soup=bs(html,'html.parser')


# Find Cerberus Hemisphere Image URL
################################################

#obtain link to page with image
    cerberus_url = hemi_soup.find('a', class_='itemLink product-item')

    cerberus_link = hemi_url+cerberus_url['href']

#connect to page with high-res image to scrape
    browser.visit(cerberus_link)
    html=browser.html
    cerb_soup=bs(html,'html.parser')

#scrape image
    cerberus = cerb_soup.find('img', class_='wide-image')

    full_cerberus = hemi_url+cerberus['src']


# Find Schiaparelli Hemisphere Image URL
################################################

#obtain link to page with image
    schia_url = hemi_soup.find_all('a', class_='itemLink product-item')

    schia_link = hemi_url+schia_url[2]['href']

#connect to page with high-res image to scrape
    browser.visit(schia_link)
    html=browser.html
    schia_soup=bs(html,'html.parser')

#scrape image
    schiaparelli = schia_soup.find('img', class_='wide-image')

    full_schiaparelli = hemi_url+schiaparelli['src']



# ### Find Syrtis Hemisphere Image URL
################################################

#obtain link to page with image
    syrtis_url = hemi_soup.find_all('a', class_='itemLink product-item')

    syrtis_link = hemi_url+syrtis_url[4]['href']

#connect to page with high-res image to scrape
    browser.visit(syrtis_link)
    html=browser.html
    syrtis_soup=bs(html,'html.parser')

#scrape image
    syrtis = syrtis_soup.find('img', class_='wide-image')

    full_syrtis = hemi_url+syrtis['src']



# ### Find Valles Hemisphere Image URL
################################################

#obtain link to page with image
    valles_url = hemi_soup.find_all('a', class_='itemLink product-item')

    valles_link = hemi_url+valles_url[6]['href']

#connect to page with high-res image to scrape
    browser.visit(valles_link)
    html=browser.html
    valles_soup=bs(html,'html.parser')

#scrape image
    valles = valles_soup.find('img', class_='wide-image')

    full_valles = hemi_url+valles['src']



# ## Hemisphere Dictionary
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": full_valles},
        {"title": "Cerberus Hemisphere", "img_url": full_cerberus},
        {"title": "Schiaparelli Hemisphere", "img_url": full_schiaparelli},
        {"title": "Syrtis Major Hemisphere", "img_url": full_syrtis}
    ]


