REM : @ECHO OFF 
REM : Runs scripts to download the new files, clean them, make the ebook, polish it, and convert it to other formats

py -3 wget_test_list.py REM : IF IT FAILS, PUT YOUR DIRECT PYTHON 3 PATH HERE
ECHO Ran Download of new files
py -3 parse_html_rec_wget.py REM : IF IT FAILS, PUT YOUR DIRECT PYTHON 3 INSTALL HERE
ECHO Ran Cleaning of files
py -2 create_epub_pypub.py REM : IF IT FAILS, PUT YOUR DIRECT PYTHON 2 INSTALL HERE
ECHO Ran creation of EPUB file
ebook-convert result.epub  temp_epub.epub --change-justification justify --cover cover.jpg --authors viivpkmn --title " Summary of A Song of Ice and Fire vol. 1-5" --publisher viivpkmn
ebook-polish temp_epub.epub asoiaf-summary.epub --cover cover.jpg
ebook-convert asoiaf-summary.epub asoiaf-summary.mobi
ebook-convert asoiaf-summary.epub asoiaf-summary.azw3
ebook-convert asoiaf-summary.epub asoiaf-summary.pdf
DEL result.epub
DEL temp_epub.epub
PAUSE