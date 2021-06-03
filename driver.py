import crawler
import os

# Load seeds
URLseed = open('seeds.txt', 'r')
URLS = [url for url in URLseed.read().split()]

pages = int(input('Enter number of pages that you want to crawl: '))

# Call the crawler
crawler.crawler(URLS,pages)