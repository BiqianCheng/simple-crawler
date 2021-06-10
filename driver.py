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
    
def display():
    try:
        print('Printing all existing seeds: \n')
        file = open('seeds.txt','r')
        counter = 1
        for line in file.readlines():
            print(counter,'.',line)
            counter += 1
        print('\n')
    except:
        print('Could not open seeds.txt!')

def changeSeeds():
    while True:
        print('Would you like to:')
        print('1. Add one seed into seeds.txt')
        print('2. Delete one seed from seeds.txt')
        print('3. Go back to main menu')
        seedCho = int(input('Enter your choice: '))
        print('\n')
        if seedCho == 1:
            file = open('seeds.txt','a')
            newSeed = input('Enter the seed: ')
            if 'https://' or 'http://' not in newSeed:
                newSeed = 'https://' + newSeed
            if '.edu' not in newSeed:
                print('\nWarning: This is not a edu page, do you still wish to continue? (y/n)')
                cont = input('')
                if cont == 'n':
                    print('Got it! This seed will not be saved into seeds.txt\n')
                    continue
                else:
                    print('Got it! Seed will be added into seeds.txt')
                    print('Disclaimer: This crawler is not designed for non edu page, do it at your own risk!\n')
            file.write('\n')
            file.write(newSeed)
            file.close()
            print('Seed has been added into seeds.txt!\n')
        elif seedCho == 2:
            rfile = open('seeds.txt','r')
            lines = rfile.readlines()
            rfile.close()
            display()
            delSeed = input('Enter the seed that you want to delete: ')
            wfile = open('seeds.txt','w')
            for line in lines:
                if line != delSeed and not line.isspace() :
                    wfile.write(line)
            wfile.close()
            print('Seed has been deleted!\n')
        elif seedCho == 3:
            break

# UI
print('Welcome to Blablabla\'s crawer\n')

while True:
    print('Choose one of the options below to proceed:')
    print('1. Call the crawler')
    print('2. Display all the seeds')
    print('3. Make changes to seeds.txt')
    print('4. Parse existed html')
    print('0. Quit')
    choice = int(input('Enter your choice: '))
    print('\n')

    if choice == 1:
        # Crawl
        crawling()
    elif choice == 2:
        # 2
        display()
    elif choice == 3:
        # 3
        changeSeeds()
    elif choice == 4:
        # Parse html
        parsing()
    elif choice == 0:
        break
    
