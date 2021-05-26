import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, urls=[], pgs=1):
        self.visited_urls = []
        self.urls_to_visit = urls
        self.numPage = pgs

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        htmlFile = url.replace('https://','').replace('.','_').replace('/','')+'.txt'
        #print(htmlFile)
        
        html = self.download_url(url)
        #folder.write(html)
        #folder.close()
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)
        print(html)
        htmlOutput = open('html/'+htmlFile,'w',encoding='utf-8')
        htmlOutput.write(html)
        htmlOutput.close()

    def run(self):
        crawledPg = 0
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            if crawledPg == numPage:
                print('\nCrawling finished!\n')
                break;
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
                crawledPg += 1

if __name__ == '__main__':
    wantedPg = int(input('Enter number of pages that you want to crawl: '))
    crw = Crawler(urls=['https://www.cs.ucr.edu'],wantedPg).run()
