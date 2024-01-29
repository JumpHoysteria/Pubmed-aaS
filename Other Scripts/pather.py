from getIDList import getUIDList
# query_path = "C:/Users/Alex/Desktop/PaperScreening"


# with open('C:/Users/Alex/Desktop/PaperScreening/Query.txt', 'r') as f:
#     text = f.read()
#     text = str(text)
#     n = text.find('END_COMMENT') + len('END_COMMENT')
#     print(n)

# text = str(text[n:len(text)])
# text = text.strip()
# print(text[0:380])

with open('C:/Users/Alex/Desktop/PaperScreening/PDF Generator/PDFGenerator/Neuer Ordner/Query.txt', 'r') as f:
    query = f.read()
    query = str(query)
    n = query.find('END_COMMENT') + len('END_COMMENT')

query = str(query[n:len(query)]).strip()
uid_list_from_program, content = getUIDList(query)
print("Amount of UID's from API: " + str(len(uid_list_from_program)))

with open('C:/Users/Alex/Desktop/PaperScreening/PDF Generator/PDFGenerator/Neuer Ordner/PMIDFROMPUBMEDOriginale.txt', 'r') as f:
    text = f.read()
    text = str(text)
    #print(text)
    lo = text.splitlines()
    print("Amount of UID's from Manual Search: " + str(len(lo)))

not_in_program = []
not_in_pubmed = []

for el in lo:
    if el not in uid_list_from_program:
        #print(el)
        not_in_program.append(el)

for el in uid_list_from_program:
    if el not in lo:
        #print(el)
        not_in_pubmed.append(el)

print(str(len(not_in_program)))
print(str(len(not_in_pubmed)))