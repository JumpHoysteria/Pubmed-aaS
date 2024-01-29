from getIDList import getUIDList


counter_miss = 0
counter_total = 0

with open('ValidationPMID.txt', 'r') as f:
    Validation_Set = f.read()
    Validation_Set = Validation_Set.splitlines()
    f.close()

with open('C:/Users/Alex/Desktop/PaperScreening/Query.txt', 'r') as f:
    query = f.read()
    query = str(query)
    n = query.find('END_COMMENT') + len('END_COMMENT')
    query = str(query[n:len(query)]).strip()

uid_list, content  = getUIDList(query)

for pmid in Validation_Set:
    counter_total += 1
    if pmid not in uid_list:
        counter_miss += 1
        print("Missing: " + pmid)

missed_relative = round(100*(100 * ((counter_total - counter_miss) / counter_total )))/100

print("Validation Result: " + str(missed_relative) + "% (bigger is better)")