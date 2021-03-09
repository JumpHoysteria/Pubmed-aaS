import json
import xml.etree.ElementTree as ET
from getIDList import getUIDList 
from getArticleInformation import getArticleInformation

##
# If there is no DOI associated, then the entry in the article-dictionary will be NONE

Query ="TEST"

uid_list = getUIDList(Query)
#print("Print ID_List:", uid_list)

article_consumed = getArticleInformation(uid_list) 
# article_consumed has the form {1: {'uid': '', 'title': '', 'authors': '', 'doi': ''}, 2: {'uid': '', 'title': '', 'authors': '', 'doi': ''},


for article in article_consumed:
    print(article_consumed[article]['doi'])