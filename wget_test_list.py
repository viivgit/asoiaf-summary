# -*- coding: utf-8 -*-
"""
@author: viivgit

Download only the needed files from the wiki with a 'whitelist' provided externally
"""
import os
import shutil

shutil.rmtree('chapters_new',ignore_errors=True)

url_list = 'chapters_to_download.txt'
os.system('wget --directory-prefix=./chapters_new/ --convert-links −−adjust−extension --input-file='+url_list) # --restrict-file-names=windows may be useful
