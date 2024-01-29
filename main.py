import markdown, datetime, mdutils, os
from getIDList import getUIDList 
from getArticleInformation import getArticleInformation
from xhtml2pdf import pisa
from string import Template

dirname = os.path.dirname(__file__)

start = "2023/12/04" ## YYYY/MM/DD
end = "2024/12/17"

##
# If there is no DOI associated, then the entry in the article-dictionary will be NONE
# 
#
#
#
##

for person in ['230308_Alex.txt','230308_Alexander.txt','230308_Antonis.txt','230308_Dipta.txt','230308_Marlene.txt','230308_Marta.txt','230308_Pallavi.txt','230308_Sabrina.txt','230308_Yan.txt']:
#for person in ['230308_Alexander.txt']:

    PATH_TO_JournalQuery = os.path.join(dirname, 'Queries/' + person)
    #PATH_TO_JournalQuery = os.path.join(dirname, 'Queries/' + '230308_Marta.txt')
    PATH_TO_BigQuery = os.path.join(dirname, 'Queries/Query.txt')
    PATH_TO_AuthorQuery = os.path.join(dirname, 'Queries/PaperScreening_Date_Author_Exclusion.txt')

    NAME_OF_Output = (file_name := person) 


    # file_name = NAME_OF_Output 


    def convert_html_to_pdf(source_html, output_filename, style):
        # From xhtml2pdf-Docs
        # open output file for writing (truncated binary)

        result_file = open(output_filename, "w+b")

        # convert HTML to PDF
        pisa_status = pisa.CreatePDF(
                source_html,                # the HTML to convert
                dest=result_file,
                default_css=style
                )           # file handle to recieve result

        # close output file
        result_file.close()                 # close output file

        # return False on success and True on errors
        return pisa_status.err

    MODE = "JOURNALS" ## Either COMBINED, AUTHORS or JOURNALS


    day = datetime.datetime.now()
    day = str(day.date())


    if MODE == "COMBINED":
        with open(PATH_TO_BigQuery, 'r') as f:
            query = f.read()
            query = str(query)
            n = query.find('END_COMMENT') + len('END_COMMENT')
            #print(n)
        query = str(query[n:len(query)]).strip()

    elif MODE == "AUTHORS":
        with open(PATH_TO_AuthorQuery, 'r') as f:
            query = f.read()
            query = str(query)
            n = query.find('END_COMMENT') + len('END_COMMENT')
        query = str(query[n:len(query)]).strip()
        
    elif MODE == "JOURNALS":
        with open(PATH_TO_JournalQuery, 'r') as f:
            query = f.read()
            query = str(query)
            n = query.find('END_COMMENT') + len('END_COMMENT')
        query = str(query[n:len(query)]).strip()
        
        query = query.replace("START", start)
        query = query.replace("END", end)
        #print(query)
       
    else:
        raise Exception('WRONG MODE SET')

    uid_list, content  = getUIDList(query)
    article_consumed = getArticleInformation(uid_list) 
    doc_title = file_name.split("_")
    doc_title = doc_title[1]
    doc_title = doc_title[:-4]
    mdFile = mdutils.MdUtils(file_name= file_name,title=doc_title)
    
    TotAmoFrJo = str(article_consumed).count('journal\': \'Nat Commun')
    NatComm_counter = 1
    
    for article in article_consumed:
            
        art = article_consumed[article]
        doi = art['doi'] # title, authors, date, journal, link (doi)
        journal = art['journal']
        date = art['date']
        author_string = ""
        title = art['title']
        #breakpoint()
        
        if person == '230308_Marta.txt' and NatComm_counter > TotAmoFrJo//2 and journal =='Nat Commun':
            NatComm_counter += 1
            continue
        elif person == '230308_Marlene.txt' and NatComm_counter <= TotAmoFrJo//2 and journal =='Nat Commun':
            NatComm_counter += 1
            continue
        elif journal == 'Nat Commun':
            NatComm_counter += 1
         

        for author in art['authors']:
            author_string = author_string + str(author) + ", "

        author_string = author_string[:-1]
        
        

        # mdFile.new_header(level=4, title=title, add_table_of_contents='n')
        # mdFile.write(str(author_string) + " " + str(date) + ", ", bold_italics_code='i')
        # mdFile.write(str(journal), bold_italics_code = 'b')
        
        # if doi == "NONE":
            # mdFile.new_header(level=6, title='No Link!', add_table_of_contents='n')
        # else:
            # link = 'https://www.doi.org/' + doi
            # mdFile.new_header(level=6, title=mdutils.tools.TextUtils.text_external_link(link, link=link), add_table_of_contents='n')
        
        # mdFile.new_paragraph('____________________________________'*9 + "\n")    
       
        
        
        mdFile.write(str(title) + " " + str(journal), bold_italics_code = 'b')
        mdFile.write(", " + str(date) + "\n")

        
        mdFile.new_paragraph(str(author_string), bold_italics_code='i')
        
        if doi == "NONE":
            mdFile.new_header(level=6, title='No Link!', add_table_of_contents='n')
        else:
            link = 'https://www.doi.org/' + doi
            mdFile.new_header(level=6, title=mdutils.tools.TextUtils.text_external_link(link, link=link), add_table_of_contents='n')
        mdFile.new_paragraph('____________________________________'*9 + "\n") 
        


    mdFile.create_md_file()


    with open(file_name + '.md', 'r', encoding='utf-8') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open(file_name + '.html', 'a+', encoding='utf-8') as f:

        HEAD = '''<!doctype html><html lang="en-US"><head></head><body>'''
        BOTTOM = '''</body>'''
        f.write(HEAD)
        f.write(html)
        f.write(BOTTOM)
        f.close()

    pisa.showLogging()

    # style is taken from xhtml2pdf-default CSS with margin set from "1em 0" to "0px"!

    style="""
    html {
        font-family: Helvetica;
        font-size: 10px;
        font-weight: normal;
        color: #000000;
        background-color: transparent;
        margin: 0;
        padding: 0;
        line-height: 0%;
        border: 1px none;
        display: inline;
        width: auto;
        height: auto;
        white-space: normal;
    }
    b,
    strong {
        font-weight: bold;
    }
    i,
    em {
        font-style: italic;
    }
    u {
        text-decoration: underline;
    }
    s,
    strike {
        text-decoration: line-through;
    }
    a {
        text-decoration: underline;
        color: blue;
    }
    ins {
        color: green;
        text-decoration: underline;
    }
    del {
        color: red;
        text-decoration: line-through;
    }
    pre,
    code,
    kbd,
    samp,
    tt {
        font-family: "Courier New";
    }
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        font-weight:bold;
        -pdf-outline: true;
        -pdf-outline-open: false;
    }
    h1 {
        /*18px via YUI Fonts CSS foundation*/
        font-size:138.5%;
        -pdf-outline-level: 0;
    }
    h2 {
        /*16px via YUI Fonts CSS foundation*/
        font-size:123.1%;
        -pdf-outline-level: 1;
    }
    h3 {
        /*14px via YUI Fonts CSS foundation*/
        font-size:108%;
        -pdf-outline-level: 2;
    }
    h4 {
        -pdf-outline-level: 3;
    }
    h5 {
        -pdf-outline-level: 4;
    }
    h6 {
        -pdf-outline-level: 5;
    }
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    pre,
    hr {
        margin:0;
    }

    p {
        margin: 2px 0px 3px 0px;
    }

    address,
    blockquote,
    body,
    center,
    dl,
    dir,
    div,
    fieldset,
    form,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    hr,
    isindex,
    menu,
    noframes,
    noscript,
    ol,
    p,
    pre,
    table,
    th,
    tr,
    td,
    ul,
    li,
    dd,
    dt,
    pdftoc {
        display: block;
    }
    table {
    }
    tr,
    th,
    td {
        vertical-align: middle;
        width: auto;
    }
    th {
        text-align: center;
        font-weight: bold;
    }
    center {
        text-align: center;
    }
    big {
        font-size: 125%;
    }
    small {
        font-size: 75%;
    }
    ul {
        margin-left: 1.5em;
        list-style-type: disc;
    }
    ul ul {
        list-style-type: circle;
    }
    ul ul ul {
        list-style-type: square;
    }
    ol {
        list-style-type: decimal;
        margin-left: 1.5em;
    }
    pre {
        white-space: pre;
    }
    blockquote {
        margin-left: 1.5em;
        margin-right: 1.5em;
    }
    noscript {
        display: none;
    }
    """
    
    end_filecomp = end.split("/")
    res = ""
    for idx, i in enumerate(end_filecomp):
        if idx == 0:
            i = i[2:]
        res += i
    end_filecomp = res
    if not convert_html_to_pdf(html, dirname + '\\output/' + end_filecomp + file_name[6:-4] + '.pdf', style):
        print("PDF IS READY!")

    for ending in [".md", ".html"]:
        os.remove(file_name + ending)