# CS172-Project

## Team member 1 - Jim Poon
## Team member 2 - Qi Qi
## Team member 3 - Shuang Zhou
## Team member 4 - Biqian Chen

# Short explanation of our design
The whole project is driven by several parts:
Languages used: Python, css JaveScript, HTML
1. Crawler
   a. Crawl the urls given in seeds.txt using "request" and "urllib.parse" library
   b. Detect duplicate pages during crawling (this page will not be counted)
   c. Has a crawl history stored into a text file(history.txt)
2. Parser
   a. Parse the html files that are crawled by the crawler using "BeautifulSoup" library
   b. Using BeautifulSoup to parse body and title text from html files
   c. Return a list consisting current html's body text, title, and urllib
3. Driver
   a. The main function that drives the crawler, parser, and a small file system related to seeds.txt
   b. File system of seeds.txt:
      i. The system enables the user to add or subtract seeds from seeds.txt
	  ii. If the user does not enter a '.edu' seed whlie adding, a warning will be shown
	  iii. All new seeds added into the seeds.txt will automatecally be add a prefix of "https://" if it does not exist
4. 	  