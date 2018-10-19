#!/usr/bin/env python
# -*- conding:utf-8 -*-
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import lxml

class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print('传入url为空，或者文本解析为空')
            return
        #print('有url和文本传来')
        soup = BeautifulSoup(html_cont, 'lxml')
        #print(soup)   这里正常
        #print(page_url)   page_url 是最开始的URL
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        #print(new_urls)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #print('创建了新的URL集合')
         #<a target="_blank" href="/item/%E7%88%B1%E5%A5%BD%E8%80%85">爱好者</a>
        #找到主内容class=‘main-content’
        #print(soup)  a href="/item/%E6%95%99%E5%AD%A6" target="_blank"
        main_cont = soup.find_all(attrs={'target': '_blank'})
        #print('获取所有连接的列表')
        for simple_link in main_cont:
            new_url = simple_link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            #print('新的URL列表')
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title">
        title_node = soup.find(class_='lemmaWgt-lemmaTitle-title').find('h1')
        #获取h1里的文本，并赋给title
        res_data['title'] = title_node.string
        #<div class="para" label-module="para">Python 是一门>
        lemma = soup.select('.lemma-summary .para')
        #print(lemma)
        #获取内容
        res_data['summary_node'] = lemma
        return res_data




