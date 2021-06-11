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
    soup = BeautifulSoup(htmlPage, 'html.parser')
    page_title = soup.find('title')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    print('Parsing done, all text in body tag will be stored in body.txt\n')
    return u" ".join(t.strip() for t in visible_texts)
