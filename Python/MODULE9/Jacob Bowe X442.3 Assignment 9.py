import os
import re
import urllib.request as urllibr

file_total = 0

# check each file and sub directory in a designated folder
for roots,dirs,files in os.walk('.\MODULE9'):

    # for each file, print the treepath
    for file in files:
        print(os.path.join(roots,file))
    #count the number of files in the directory
    file_count = len(files)
    file_total += file_count
    #print the number of files in the sub directory
    print("file count: ",file_count)
#print total number of files 
print('file total:', file_total)

##Sample : <img src="img_chania.jpg" alt="Flowers in Chania">
## re : ^(<img)(.*)(>)

#setup the RegEx to search for within URL source file
findimg = re.compile("(<img)(.*)(>)") #this regex hates me in VS Code no idea why

#open/read website
website = urllibr.urlopen('https://secho.neocities.org/module_5/SSRS/gallery.html')
html = str(website.read())
website.close()

#find all RegEx matches within the website
imgs = findimg.findall(html)
for entry in imgs:
    for value in entry:
        print(value)
