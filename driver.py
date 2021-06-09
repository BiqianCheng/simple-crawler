import crawler
import parse
import os

def crawling():
    # Load seeds
    URLseed = open('seeds.txt', 'r')
    URLS = [url for url in URLseed.read().split()]
    pages = int(input('Enter number of pages that you want to crawl: '))

    # Call the crawler
    crawler.crawler(URLS,pages)

def parsing():
    file = input('Enter the htmlFile that you want to parse(including the path if not in the same directory): ')
    parse.parse(file)

# UI
print('Welcome to Blablabla\'s crawer\n')

while True:
    print('Choose one of the options below to proceed:')
    print('1. Call the crawler')
    print('2. Display all the seeds (WIP)')
    print('3. Add seed(s) into seeds.txt (WIP)')
    print('4. Parse existed html')
    print('0. Quit')
    choice = int(input('Enter your choice: '))
    print('\n')

    if choice == 1:
        # Crawl
        crawling()
    elif choice == 2:
        # 2
        print('2')
    elif choice == 3:
        # 3
        print('3')
    elif choice == 4:
        # Parse html
        parsing()
    elif choice == 0:
        break
    
