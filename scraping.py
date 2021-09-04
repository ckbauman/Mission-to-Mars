
# 10.3.3
# Import Splinter and BeautifulSoup and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# HTML parser - convert the browser html to a soup object then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# assign title and summary text to variables - narrowing down in the website
# use .find to get specific
# we know the title has div and class of content_title
slide_elem.find('div', class_='content_title')

# only want the text and not extra HTML stuff
# Use the parent element to find the first `a` tag and save it as `news_title`
# use .get_text to only get text of the element returned
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# find the summary of the first article which is most recent article
# Use the parent element to find the paragraph text
# .find() gets the first class and attribute with the specifics
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# # 10.3.4 Scrape Mars Data: Featured Image

# Visit URL to get the full image
url = 'https://spaceimages-mars.com'
browser.visit(url)

# get the full image by clicking on the button on the webpage
# Find and click the full image button
# using spinter, click the second button [1]
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
# BeautifulSoup looks inside <img /> tag for image with class of fancybox-image
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
# create a complete URL by adding base URL to the partial URL created above
# create variable img_url to hold the f string
# f string formatting to print in Python
# curly brackets hold variable inserted into the f string
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# # 10.3.5 Scrape Mars Data: Mars Facts

# read table information using Pandas read_html()
# read_html() specifically searches for and returns a list of tables found in HTML
# index of 0 tells Pandas to pull only the first table it encounters

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# convert the df back into HTML
df.to_html()

# when done scraping, turn off automated browsing session
# better for computer memory

browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




