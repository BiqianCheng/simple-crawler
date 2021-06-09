from bs4 import BeautifulSoup

def parse(file):
    # Empty the file first
    f = open(file,'r',encoding='utf-8')
    f.close()
    f = open(file,'r',encoding='utf-8')
    #page = f.read()
    #print(page)
    soup = BeautifulSoup(f,'html.parser')
    # Get all text from body tag
    tag = soup.body
    # Output to body.txt
    tempTxt = open('body.txt','w',encoding='utf-8')
    for string in tag.strings:
        if not string.isspace():
            tempTxt.write(string)
    
    tempTxt.close()
    print('Parsing done, all text in body tag will be stored in body.txt\n')
        