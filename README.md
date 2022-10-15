# Web Scrapping- Stock Exchange Project

## Disclaimer: 
### My client allowed permission to publish this project

This repository contain scrapper for a stock exchange project whose objective was to study how news affect stock prices for 8 Jamaica based companies. The crawler was designed and implemented in _**scrapy**_ a python package/framework for web crawlers.

The crawler functionalities reside in _jamaica.py_ file. The crawler inherits from the basic _Spider_ class of scrapy.

_start_requests()_ function initiates the crawler using the provided keyword and page number. **keyword** is a specific company's stock trading symbol. The bot sends a search request tothe website search box using this keyword. Page number is the search result page numbers at the bottom. After visiting each link the crawler calls _**parse()**_ function and passes the response data to it. 

_**parse()**_ function converts response to bs4 object and extracts all news article from that search result page, store the links in a list and pass that list to _**parse_articles()**_ function. 

_**parse_articles()**_  function extracts article's date, headline and content, each is stored in its respective df column. When all links are scrapped, the final data frame is stored in a csv file. 

## Files 
_items.py_ scrappy items or basically features of the data to be extracted are defined here. 

_pipeline.py_ any data wrangling and writing is defined in this files

_settings.py_ crawler rules reside here.

_middlewares.py_ any transaction with third party tools are defined here, for example rotating ip address 

