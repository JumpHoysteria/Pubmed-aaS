import requests
import xml.etree.ElementTree as ET


def getUIDList(query):
    idlist = []
    XPath = "./IdList/Id"
    db = "pubmed"
    query = "eyes"
    retmax = "10" #MAX 400
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db={db}&term={query}&retmax={retmax}'

    r = requests.get(url)
    #print(r.content)

    tree = ET.fromstring(r.content)
    tree = tree.findall(XPath)

    for child in tree:
        idlist.append(child.text)


    return idlist