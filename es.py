import sys
from elasticsearch import Elasticsearch
from datetime import datetime


elastic_pass = "FE0Yrg2pU5jxf0Ea7V7a5d5l"
elastic_endpoint = "https://cs172-project-ad1cfb.es.eastus2.azure.elastic-cloud.com:9243"

esConn = Elasticsearch(
    cloud_id="cs172-project:ZWFzdHVzMi5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDQzYTcyYzM3YTQ3OTQyNWZiMGVhZDRmZDRlMDE3ZWQyJGEzNjhkZWExOTBkZjRiM2FiNmRlN2E3ZWJkMmQ0M2Y2", http_auth=("elastic", "FE0Yrg2pU5jxf0Ea7V7a5d5l"))

# doc = {
#     "url": "https://ucsd.edu",
#     "page_title": "University of California San Diego",
#     "text": "<p>Top public university in the nation for contributions to social mobility, research and public service.</p>",
#     "timestamp": datetime.now(),
#     "author": ""
# }


def uploadDoc(ESList):
    """Upload docmuent to ElasticSearch
    
    Args: doc (object): A doc object that contain url, page_title, text, timestamp and author.
    ```
    {
        "url": "https://www.example.com",
        "page_title": "University of California San Diego",
        "text": "<p>Top public university in the nation for contributions to social mobility, research and public service.</p>",
        "timestamp": datetime.now(),
        "author": ""
    }
    ```
    """
    try:
        doc = {
            "url": ESList[0],
            "page_title": ESList[1],
            "text": ESList[2],
            "timestamp": datetime.now(),
            "author": ""
        }
        res = esConn.index(index="edusite", body=doc)
        print(res)
        print('\n')
    except ConnectionError as err:
        print("Unexpected error: {}".format(err))

# def bulkLoad(docs):
