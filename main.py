import json, markdown, datetime
import mdutils
import xml.etree.ElementTree as ET
from getIDList import getUIDList 
from getArticleInformation import getArticleInformation
import pypandoc
from xhtml2pdf import pisa

##
# If there is no DOI associated, then the entry in the article-dictionary will be NONE

def convert_html_to_pdf(source_html, output_filename):
    # From xhtml2pdf-Docs
    # open output file for writing (truncated binary)

    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

#query_path = "C:/Users/Alex/Desktop/PaperScreening"


with open('C:/Users/Alex/Desktop/PaperScreening/Query.txt', 'r') as f:
    query = f.read()
    query = str(query)
    n = query.find('END_COMMENT') + len('END_COMMENT')
    #print(n)

query = str(query[n:len(query)]).strip()

#print(query)

uid_list, content  = getUIDList(query)
#print("Print ID_List:", uid_list)

article_consumed = getArticleInformation(uid_list) 

#print(len(article_consumed))

# article_consumed has the form {1: {'uid': 'UID', 'title': 'TITLE', 'authors': '['AUTHOR1', 'AUTHOR2']', 
# 'doi': 'DOI'}, 2: {'uid': 'UID', 'title': 'TITLE', 'authors': '['AUTHOR1', 'AUTHOR2']', 
# 'doi': 'DOI'}, ... }


# for article in article_consumed:
#     print(article_consumed[article]['title'])

day = datetime.datetime.now()
day = str(day.date())

file_name = 'Paper_of_Interest_' + day

mdFile = mdutils.MdUtils(file_name= file_name,title=file_name)

for article in article_consumed:
    
    mdFile.new_header(level=4, title=article_consumed[article]['title'], add_table_of_contents='n')

    doi = article_consumed[article]['doi']
    
    if doi == "NONE":
        mdFile.new_header(level=6, title='No Link!', add_table_of_contents='n')
    else:
        mdFile.new_header(level=6, title=mdutils.tools.TextUtils.text_external_link("Link", link='https://www.doi.org/' + doi), add_table_of_contents='n')
    


mdFile.create_md_file()


with open(file_name + '.md', 'r', encoding='utf-8') as f:
    text = f.read()
    html = markdown.markdown(text)

with open(file_name + '.html', 'w', encoding='utf-8') as f:
    f.write(html)

pisa.showLogging()
print(convert_html_to_pdf(html, 'letgo.pdf'))

# https://github.com/xhtml2pdf/xhtml2pdf
# https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-to-convert-markdown-text-to-html
# https://stackoverflow.com/questions/4135344/is-there-any-direct-way-to-generate-pdf-from-markdown-file-by-python
# 

