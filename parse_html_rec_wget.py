# -*- coding: utf-8 -*-
"""
@author: viivgit

Parse all files and clean them to have just the wanted output: Text, Nav, Places
"""
from bs4 import BeautifulSoup
import os
import re
import shutil

shutil.rmtree('clean',ignore_errors=True)

count = 0 # for the mkdir, do it only at first pass

for htmlfile in os.listdir("./chapters_new"):
    file_name, file_ext = os.path.splitext(htmlfile)
    print(file_name)
    soup = BeautifulSoup(open("./chapters_new/"+htmlfile, encoding='utf-8'))
    
    [s.extract() for s in soup('script')] # removes anything between <script>...</script> included
    [s.extract() for s in soup('meta')] # removes anything between <meta>...</meta> included
    [s.extract() for s in soup('link')] # removes anything between <link>...</link> included
    [s.extract() for s in soup('ul')] # removes anything between <ul>...</ul> included
    
#    match = re.search(r'<tbody><tr><th colspan="2" style="text-align:center; font-size:125%; font-weight:bold; background-color: (#.*>)(.*)</th></tr>', str(soup)) # get title character
#    match = re.search(r'<td style="width:33%; text-align:center; vertical-align:middle; padding-right:0.1em; padding-left:0.1em;"><a class="mw-selflink selflink">(.*)</a></td>', str(soup)) # get title character
    match = re.search(r'<td style="width:33%; text-align:center; vertical-align:middle; padding-right:0.1em; padding-left:0.1em;"><?(.*)>?</td>', str(soup)) # get title character
    #    title = match.group(2) if match else None
    title = match.group(1) if match else None
    match11 = re.search(r'>',title)
    if match11:
        title = re.sub(r'.*>(.*)</a>', r'\1', title)
    
    if (title != ('Prologue' or 'Epilogue')):
        str1temp=re.sub(r' - A Wiki of Ice and Fire',': '+title,soup.find('title').string) # removes '- A Wiki of Ice and Fire' from chapter title, and add character
    else:
        str1temp=re.sub(r' - A Wiki of Ice and Fire','',soup.find('title').string) # removes - A Wiki of Ice and Fire from chapter title, does not add Prologue/Epilogue since they are already there
    
    str1temp=re.sub(r'-',' - ', str1temp, 1) # puts space around the hyphen between Book and Chapter. Only first match in case in the future the name of a chapter has an hyphen in it
    
    str2temp=u'<h1 id="firstHeading" class="firstHeading page-header" lang="en"><span dir="auto">'+str1temp+'</span></h1>'
    soup.head.insert_after(str2temp) #insert title at the top
    
    soup.title.string = str1temp # to also change the chapter names in the Table of Contents
    
    str3temp=str(soup).replace(r'&lt;',r'<').replace(r'&gt;',r'>') # removes what I believe are Unicode artifacts
    
    with open("temp_stripped.html","w",encoding='utf-8') as file:
        file.write(str3temp)
    
    with open('temp_stripped.html','r',encoding='utf-8') as f:
        text = f.read()

#        text = re.sub(r'/index.php/','', text) # removes '/index.php/' for functional links

#        text = re.sub(r'(<h2>Navigation menu</h2>.*</tbody></table></th></tr>)','', text, flags=re.S) # removes Navigation pane (only vor v1.0)
#        text = re.sub(r'(<div class="navbar navbar-default.*<tr><th>Place)','<tr><th><b>Place: </b>', text, flags=re.S) # removes top of Navigation pane (only vor v1.1)
        text = re.sub(r'(<div class="navbar navbar-default.*<tr><th scope="row">Place</th><td>)','<tr><th scope="row"><b>Place(s): </b></th><td>', text, flags=re.S) # removes top of Navigation pane
        text = re.sub(r'(<tr><th scope="row">Page</th><td>.*Other versions</a>\)</small></td></tr>)','', text, flags=re.S) # removes Page info
#        text = re.sub(r'(<tr><th colspan="2" style="text-align:center;">Chapter chronology.*Chapters">All</a>\)</small></th></tr>)','', text) # removes link to all chapters (only vor v1.1)
        text = re.sub(r'(<tr><th colspan="2" style="text-align:center;background-color: #.*Chapters">All</a>\)</small></th></tr>)','', text) # removes link to all chapters
        text = re.sub(r'(<td style="width:33.*Appendix.*</td>)','', text) # removes Appendix links
#        text = re.sub(r'(<tr><th colspan="2">)','<br>\n<br>\n<th><b>Navigation: </b></th>\n<tr><th colspan="2">', text) # Adds text 'Navigation' (only vor v1.1)
        text = re.sub(r'(<tr><td colspan="2" style="text-align:center">\n)','<br>\n<br>\n<th><b>Navigation: </b></th>\n<tr><td colspan="2" style="text-align:center">', text, 1) # Adds text 'Navigation'

        match2 = re.search(r'<tr><td colspan="2" style="text-align:center">(<(i|a)+.*)', text) # catches the first row (previous chapter in time)
        if match2:
            nav2 = match2.group(1) # transforms it in text
            text = re.sub(nav2, '', text) # delete useless text, could be improved to delete whole line
            text = re.sub(r'(<tbody>)', '<tbody>\n<tr>\n<td style="width:33%; text-align:center; vertical-align:middle;" colspan="5">'+nav2, text, 1) # put back the match text in good place

#        match3 = re.search(r'(?s:.*)<tr><td colspan="2" style="text-align:center">(.*)</a></td></tr></tbody></table>', text, flags=re.S) # catches the last row (next chapter in time)
#        match3 = re.search(r'(?s:.*)<tr><td colspan="2" style="text-align:center">\n(.*?)</td></tr></tbody></table>', text, flags=re.S) # catches the last row (next chapter in time)
        match3 = re.search(r'↓<br/>(.*?)</td></tr>', text, flags=re.S) # catches the last row (next chapter in time)
        if match3:
            nav3 = match3.group(0) # transforms it in text
            test1 = re.search(r'The Winds of Winter',nav3)
            if test1:
                text = re.sub(re.escape(nav3), '', text, 1, flags=re.S) # delete useless text, could be improved to delete whole line
#                text = re.sub(r'(</tr></tbody>)', '<tr>\n<td style="width:33%; text-align:center; vertical-align:middle;" colspan="5">'+nav3+'</a></td></tr></tbody>', text, count = 1)  # put external links for the Winds of Winter
            else:
                text = re.sub(nav3, '', text, flags = re.S) # delete useless text, could be improved to delete whole line
                text = re.sub(r'(</tbody></table>)', '<tr>\n<td style="width:33%; text-align:center; vertical-align:middle;" colspan="5">'+nav3+'</tbody></table>', text, 1)  # put back the match text in good place

        text = re.sub(r'(.html" title=)','-clean.html" title=', text) # modify html link to clean file
        text = re.sub(r'(<!--.*-->)','', text) # removes comments (to have a lighter file)
        text = re.sub(r'<div class="thumb tleft.*</div></div></div>','', text) # removes pics
        text = re.sub(r'<div class="thumb tright.*</div></div></div>','', text) # removes pics
        text = re.sub(r'<div class="toc" id="toc"><div class="toctitle" dir="ltr" lang="en"><h2>Contents</h2></div>','', text) # removes 'Contents' header
        text = re.sub(r'(<h2><span id="(?!S).*</body>)',r'</body>', text, flags=re.S) # removes bottom of page
        text = re.sub(r'(<h2><span class="mw-headline" id="(?!S).*</body>)',r'</body>', text, flags=re.S) # removes bottom of page (alt.)
        text = re.sub(r'(Retrieved from "<a .*</body>)',r'</body>', text, flags=re.S) # removes extra stuff at bottom of page (a few cases)
        text = re.sub(r'(<sup.*</sup>)', '', text) # removes Notes hyperlinks

        if title == 'Prologue':
            text = re.sub(r'(^.*←.*)','', text, flags = re.M) # removes extra line only in Prologue
        if title == 'Epilogue':
            text = re.sub(r'(^.*→.*)','', text, flags = re.M) # removes extra line only in Epilogue
            
        text = re.sub(r'<td style="vertical-align:middle;">→ </td>\n\n', '', text) # removes extra line in the three cases zhere there is no Epilogue after

        # section to add Navigation info at the end of chapter too for easy navigation (if not wanted just removes these next 5 lines)
#        match1 = re.search(r'(<th><b>Navigation: </b></th>.*?)\n<p>', text, flags=re.S) # get navigation info
        match1 = re.search(r'(<th><b>Navigation: </b></th>.*?)</tbody></table>', text, flags=re.S) # get navigation info
        nav = match1.group(1) if match1 else None
        
        text = re.sub(r'(</body>)', '\n'+nav+'</a></td></tr></tbody></table>'+'\n</body>', text) # put navigation info at the end
        
#        soup2 = BeautifulSoup(text)
#        
#        soup2.body.insert(len(soup2.body.contents),nav) # place navigation info at the end
#        text=str(soup2).replace(r'&lt;',r'<').replace(r'&gt;',r'>') # removes what I believe are Unicode artifacts

    if count == 0:
        os.mkdir("clean")
    os.chdir("./clean")
    with open(file_name+'-clean'+file_ext,'w',encoding='utf-8') as outf:
        outf.write(text)
    os.chdir("..")
    count = count + 1