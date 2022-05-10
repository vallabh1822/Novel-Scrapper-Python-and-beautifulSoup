"""
To scrape novel chapter from 'Boxnovel.com' and convert it in epub formats (create epub file) and return its reference
functions in module:
1.convertToEpub(doc:html, nameOfNovel)
2.BoxNovelScrape(StartChapter:int =1, EndChapter:int =2, name="ANOTHER WORLD’S VERSATILE CRAFTING MASTER"):
"""


import random
from bs4 import BeautifulSoup, Doctype
import requests
import pypandoc
import re
import time
from IPython.display import clear_output





def convertToEpub(doc,nameOfNovel):
    
     
    htmlName= nameOfNovel + ".html"
    with open(htmlName, "w",encoding='utf-8') as file:
        file.write(str(doc))
    epubName= nameOfNovel + ".epub"
    

    
    output= pypandoc.convert_file(htmlName,'epub3', outputfile=epubName)  
    file.close()
    return output



def BoxNovelScrape(StartChapter:int =1, EndChapter:int =2, name="ANOTHER WORLD’S VERSATILE CRAFTING MASTER",time_delay=10):
    doc = BeautifulSoup()

    doc.append(Doctype('html'))
    html = doc.new_tag('html', lang='en-US')
    doc.append(html)
    head = doc.new_tag('head')
    html.append(head)
    meta = doc.new_tag('meta', charset='utf-8')
    head.append(meta)
    title = doc.new_tag('title')
    title.string = name
    head.append(title)
    body = doc.new_tag('body')
    html.append(body)

    nameOfNovel =name
    nameOfNovel =nameOfNovel.lower()
    nameOfNovel= re.sub(r'[^\w\s]', '', nameOfNovel)
    nameOfNovel = nameOfNovel.replace(" ", "-")



    for i in range (StartChapter, EndChapter):
        url ="https://boxnovel.com/novel/"+nameOfNovel+"/chapter-{}/".format(i)
        r1= requests.get(url)
        time.sleep(random.random()*time_delay)
        chapter=r1.content
        soup1 = BeautifulSoup(chapter, 'html5lib')
        chapter_con = soup1.find_all('p')

        header = doc.new_tag('h1')
        header.string = "chapter {}".format(i)
        body.append(header)
        clear_output()
        print((i+1-StartChapter)*100/(EndChapter-StartChapter)  , '% Completed')
        
        # Append content to html
        for i, child in enumerate(chapter_con):
                if child==chapter_con[-21]:
                    break
                body.append(child)
       

    
    name = name + " {}-{}".format(StartChapter, EndChapter)
    output = convertToEpub(doc, name)
    return output    
