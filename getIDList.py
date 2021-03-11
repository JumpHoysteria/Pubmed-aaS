import requests
import xml.etree.ElementTree as ET


def getUIDList(query):

    idlist = []
    XPath = "./IdList/Id"
    db = "pubmed"
    #query = "eyes"
    retmax = "10000" #MAX 400
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db={db}&term={query}&retmax={retmax}'

    r = requests.get(url)
    print("Status code: " + str(r.status_code))

    tree = ET.fromstring(r.content)
    tree = tree.findall(XPath)
    print("Lenght of Id_list: " + str(len(idlist)))
    for child in tree:
        idlist.append(child.text)
        
    print("Lenght of Id_list: " + str(len(idlist)))
    return idlist, r.content

query = '''(((((
("2020/01/01"[Date - Publication] : "2021/01/01"[Date - Publication])
AND 
(
(((((((((mouse) OR (human)) OR (amphibians)) OR (zebrafish)) OR (ES cells)) OR (iPSC)) OR (rodent)) OR (chicken)) OR (avian)) OR (mammals)
)
AND
(
((((((((((((((((("Developmental Haematopoiesis" Mouse OR
"Developmental Haematopoiesis") OR
"Developmental Haematopoiesis") OR
"Umbilical cord blood") OR
((("HSC" OR "Haematopoietic Stem Cell") OR "HSPC") OR "Haematopoietic Stem and Progenitor Cell")) OR
("Aorta-Gonad-Mesonephros" OR "AGM")) OR
(("Hematopoiesis" OR"Haematopoiesis") AND (((fetal liver OR FOI) OR Notch) OR Sox17))) OR
Dorsal Aorta) OR
(("Endothelial to Haematopoietic Transition" OR "Endothelial-to-haematopoietic transition") OR "EHT")) OR
RUNX1) OR
FLK1) OR
KDR) OR
(("Intra-aortic cluster" OR "IAHC") OR "intra-aortic clusters")) OR
CD43) OR
CD41) OR
Vasculogenesis) OR
Angiopoietin) OR
Gfi1
)
OR
(
(((((((((((((((((((((((((((((((((((((((((((((((((Alexander Medvinsky[Author] OR 
Marella de Bruijn[Author]) OR 
Elaine Dzierzak[Author]) OR 
Thierry Jaffredo[Author]) OR
Catherine Robin[Author]) OR
Anna Bigas[Author]) OR
Joanna Tober[Author]) OR
Nancy Speck[Author]) OR
Hanna Mikkola[Author]) OR
Ana Cumano[Author]) OR
Igor M Samokhvalov[Author]) OR
Constanze Bonifer[Author]) OR
John E Dick[Author]) OR
Manuela Tavian[Author]) OR
Livesey FJ[Author]) OR
Guy Sauvageau[Author]) OR
Françoise Dieterlen-Lièvre[Author]) OR
Isabelle Godin[Author]) OR
David Scadden[Author]) OR
Stuart Orkin[Author]) OR
Leonard Zon[Author]) OR
George Daley[Author]) OR
Sean J Morrison[Author]) OR
Irving L Weissman[Author]) OR
Hiromitsu Nakauchi[Author]) OR
Katrin Ottersbach[Author]) OR
Aldo Ciau-Uitz[Author]) OR
Connie J Eaves[Author]) OR
Martin Gering[Author]) OR
Cristina Lo Celso[Author]) OR
Charles Durand[Author]) OR
Sten Eirik W. Jacobsen[Author]) OR
Trista North[Author]) OR
Philippe Herbomel[Author]) OR
Karima Kissa[Author]) OR
Roger Patient[Author]) OR
David Traver[Author]) OR
Igor Slukvin[Author]) OR
Andrew Elefanty[Author]) OR
Timm Schroeder[Author]) OR
Christophe Lancrin[Author]) OR
Georges Lacaud[Author]) OR
Valerie Kouskoff[Author]) OR
Michael Kyba[Author]) OR
Berthold Göttgens[Author]) OR
Thorsten M. Schlaeger[Author]) OR
Michael J. Chen[Author]) OR
Paul Frenette[Author]) OR
Keisuke Ito[Author]) OR
Shin-Ichi Nishikawa[Author]) OR
Shinya Yamanaka[Author])
)
)
NOT (Yeast)) NOT (cancer)) NOT (Insecticide)) NOT (Invertebrates)) NOT (Plants)
'''

uid_list, content = getUIDList(query.strip())