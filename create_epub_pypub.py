# -*- coding: utf-8 -*-
"""
@author: viivgit

Convert the files in ePub
"""

#import pypub
from pypubmod.epub import Epub
from pypubmod.chapter import ChapterFactory
#from pypub.clean import condense # useless in the end
import os
import re
import shutil

def noclean(a):
    return a

shutil.copy('./first_page_to_add_to_Calibre.html','./clean/first page to add to Calibre.html')

#os.chdir('../html_clean')
with open('index_including_first_page.html','r') as index:
    text = index.read()
    text = re.sub(r'(<html>.*0pt">)','', text, flags=re.S) # removes top lines
    text = re.sub(r'(</p>.*</html>)','', text, flags=re.S) # removes bottom lines
    text = re.sub(r'(<a href=")','', text, flags=re.S) # remove useless html headers from the beginning of each line
    text = re.sub(r'(">.*</a><br/>)','', text) # remove useless html headers from the end of each line
#    text = re.sub(r'(\n)','', text) 
    
    with open('temp.html','w') as file: # write to file to be able to perform the following operations
        file.write(text)
    
with open('temp.html') as f: # clean and put in list
    htmlfile = f.readlines()
    htmlfile = [x.strip() for x in htmlfile] # remove end of lines
    del htmlfile[0] # remove first empty line
    
os.chdir('./clean')

#epub = pypub.Epub('result')
epub = Epub('result')

for file in htmlfile:
    print file
    try:

#        if (title != ('Prologue' or 'Epilogue')):
#            str1temp=re.sub(r' - A Wiki of Ice and Fire',': '+title,soup.find('title').string) # removes '- A Wiki of Ice and Fire' from chapter title, and add character
#        else:
#            str1temp=re.sub(r' - A Wiki of Ice and Fire','',soup.find('title').string) # removes - A Wiki of Ice and Fire from chapter title, does not add Prologue/Epilogue since they are already there
        
#        chap = pypub.ChapterFactory(clean_function=noclean).create_chapter_from_file(file)
        chap = ChapterFactory(clean_function=noclean).create_chapter_from_file(file)
        epub.add_chapter(chap)
    except ValueError:
        pass
    
os.chdir('..')
epub.create_epub(os.getcwd())

shutil.rmtree('clean',ignore_errors=True)
shutil.rmtree('chapters_new',ignore_errors=True)
os.remove('temp.html')
os.remove('temp_stripped.html')
