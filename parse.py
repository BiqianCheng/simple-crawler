from bs4 import BeautifulSoup
from bs4.element import Comment


def tag_visible(element):
    """
    Check if the passed element is visible to the user

    Args:
        element (ResultSet): The element that need to be pass in to check

    Returns:
        bool: If the element is visible by user, return true. Otherwise return false.
    """
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def parse(htmlPage):
    """
    Parse all the text from the html pass in. Return all the text that is visible by the user.

    Args:
        htmlPage (string): The html

    Returns:
        string: The text string that is visible by the user 
    """
    htmlText = open(htmlPage,'r',encoding='utf-8')
    soup = BeautifulSoup(htmlText, 'html.parser')
    page_title = soup.find('title')
    texts = soup.findAll(text=True)
    # Find title
    titleText = soup.find('title')
    titleText = titleText.string
    print(titleText,'\n')
    # Find text
    visible_texts = filter(tag_visible, texts)
    #print('Parsing done, all text in body tag will be stored in body.txt\n')
    bodyText = u" ".join(t.strip() for t in visible_texts)
    print(bodyText,'\n')
    # Get url
    URLList = htmlPage.replace('html/','').replace('.html','').replace('_',' ').split()
    URL = ''
    hist = open('history.txt','r')
    history = hist.readlines()
    for line in history:
        isThis = False
        URL = ''
        for word in URLList:
            if word not in line:
                isThis = False
                break
            isThis = True
            URL = line
        if isThis:
            break
    #print(URL)     
