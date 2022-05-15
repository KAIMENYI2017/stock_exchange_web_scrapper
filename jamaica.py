# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:02:28 2022

@author: RONNY
"""

from scrapy import Spider
import scrapy
from bs4 import BeautifulSoup as BS
import pandas as pd

def page_num(j,s,e):
    page=[]
    for i in range(s,e):
        j=j-10
        if j>0:
            j=j
            page.append(j)
        else:
            j=0
            page.append( j)
    return page


class JamaicaSpider(Spider):
    name ="jamaica"   
    keyword="Carreras"
    
    
    
    def start_requests(self):
        j=370
        s=0
        e=37
        page=[]
        for i in range(s,e):
            j=j-10
            if j>0:
                j=j
                page.append(j)
            else:
                j=0
                page.append(j)
        
        
        for p in page:
            url=f"https://www.jamaicaobserver.com/search/?q={self.keyword}&start={p}"
            yield scrapy.Request(url, callback=self.parse)
        

       
    def parse(self, response):
        soup = BS(response.text, 'lxml')
        data=soup.select('.entry-title')
        links=[]
        for h in data:
            url = h.find('a').get('href')
            links.append(url)

        for article in links:
            yield scrapy.Request(url=article, callback=self.parse_articles)
                

    def parse_articles(self, response):
        articles_db={"Date":[],"Date_updated":[], "Title":[], "Content":[]}
        date1=response.css('.article-pubdate::text').get()
        date2=response.css('.article-modifieddate::text').get()
        title=response.css('#article-body > div:nth-child(1) > div:nth-child(2)::text').get()
        content=[]
        content.append(response.css("strong::text").get())
        content.append(response.css("p::text").getall())
        articles_db['Date'].append(date1)
        articles_db['Date_updated'].append(date2)
        articles_db['Title'].append(title)
        articles_db['Content'].append(content)
        articles_db=pd.DataFrame(articles_db)
        articles_db.to_csv(f"E:/clients/alade/jamaica/observerData/{self.keyword}.csv", mode='a', index=False, header=False)
