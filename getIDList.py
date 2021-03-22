import requests
import xml.etree.ElementTree as ET


def getUIDList(query):

    idlist = []
    XPath = "./IdList/Id"
    db = "pubmed"
    retmax = "10000"
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db={db}&term={query}&retmax={retmax}'

    r = requests.get(url)
    #print("Status code: " + str(r.status_code))

    tree = ET.fromstring(r.content)
    tree = tree.findall(XPath)
    for child in tree:
        idlist.append(child.text)
        
    #print("Amount of Results: " + str(len(idlist)))
    return idlist, r.content