#!/usr/bin/env python
# coding: utf-8

# In[82]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[83]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=True)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


slide_elem.find("div", class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[10]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[14]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# In[17]:


### Mars Weather


# In[18]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[19]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[ ]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# In[ ]:


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles


# In[ ]:


### Hemispheres


# In[57]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[100]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# 3. Write code to retrieve the image urls and titles for each hemisphere.

hemisphere_image_urls.clear()
for i in range(0,4):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    hemispheres={}
    
    links_found=browser.links.find_by_partial_text('Enhanced')[i]
    links_found.click()
    
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    img_url=img_soup.select('a',class_='downloads')[4].get('href')
    
    for child in img_soup.select('h2')[0].children:
    
        title=child
    
    hemispheres['img_url']=img_url
    
    hemispheres['title']=title
    
    hemisphere_image_urls.append(hemispheres)


# In[101]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[102]:


browser.quit()


# In[ ]:




