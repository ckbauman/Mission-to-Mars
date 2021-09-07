# Mission-to-Mars
Module 10

## Overview
We have creted a web application that captures live data for Mars News, Mars Images and Mars Facts.  We will be adding additional Mars hemisphere images.  We will be using BeautifulSoup and Splinter to scrape full-resolution images of Mar's 4 hemispheres and the titles.



## Results
We have created a Jupyter Notebook file to pull the information needed:
- Mission_to_Mars_Challenge.ipynb

This information was exported into a python file:
- Mission_to_Mars_Challenge.py

The scraping file was created to include all the scraped data for the 4 areas:
- scraping.py

The application file was created to run the scraping.py data.  This is run and locally stored on a Mongo database:
- app.py

The web application is formatted by a html file stored in the templates folder.  This determines the layout:
- Templates/index.html


## Summary
This web application requires many steps to complete using Python's BeautifulSoup, Splinter, html5lib (parsing HTML), lxml, Selium's webdriver_manager, ChromeDriverManager, HTML/CSS and MongoDB.
