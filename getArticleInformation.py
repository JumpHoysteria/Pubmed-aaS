import xml.etree.ElementTree as ET
import requests, math

#GOOD XML PARSED WELL
#print(ET.tostring(xml, encoding='utf8').decode('utf8'))

def getArticleInformation(uid_list):
    THRESHOLD = 250

    if len(uid_list) > THRESHOLD:

        it_amount = math.ceil(len(uid_list)/THRESHOLD) - 1

        print("Amount of Iterations is: ", it_amount + 1)
        article_info = _getArticleInfo(uid_list[0:THRESHOLD])

        it_work = 0

        while it_amount != 0:

            it_amount -= 1
            it_work += 1
            #print("IT_WORK / IT_AMOUNT: ", it_work, " / ", it_amount)

            offset = THRESHOLD * it_work

            if it_amount == 0:
                end_index = len(uid_list)
            else:
                end_index = offset + THRESHOLD

            temp = _getArticleInfo(uid_list[offset:end_index])

            for i in range(len(temp)):
                article_info[i + 1 + offset] = temp[i + 1]

    else:
        article_info = _getArticleInfo(uid_list)

    return article_info


def _getArticleInfo(uid_list):
        
    uid_string = ""
    
    for child in uid_list:
        uid_string = uid_string + str(child) + ","

    uid_string = uid_string[:-1]

    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={uid_string}&version=2.0'

    r = requests.get(url)
    #print("This is the response: ", r.content)
    #print(r.content)

    xml = ET.fromstring(r.content)

    article_info = {}
    
    #for article in xml.findall(f".//*[@uid=\'{uid}\']"):
    for uid in uid_list:
        index = uid_list.index(uid) + 1
        article = xml.find(f".//*[@uid=\'{uid}\']")
            # This returns DocumentSummary for Article
            # print(ET.tostring(article, encoding='utf8').decode('utf8'))
            
        noDOI = True

        for Def in article.findall('.//ArticleId'):
            IdTypeN = Def.find('.//IdTypeN').text
            if IdTypeN == '3':
                noDOI = False
                doi = Def.find('.//Value').text

        authors = article.findall('./Authors/Author')
        author_list = []
        for author in authors:
            name = author.find('./Name').text
            author_list.append(name)

        title = article.find('./Title').text
        
        if noDOI:
            article_info[index] = {
                "uid": uid,
                "title": title,
                "authors": author_list,
                "doi": "NONE",
            }

        else: 
            article_info[index] = {
                "uid": uid,
                "title": title,
                "authors": author_list,
                "doi": doi,
            } 

    return article_info

## RESULT SHOULD BE {articles: [{"uid": "12312", "title": "Allosteric", "authors": "M. Weisskopf", "doi": "doi.org/ji"}, 
# {"uid": "21341", "titles": "Haematopoetic Niche", "authors": "A. Medvinsky", "doi": "doi.org/asd"}]}