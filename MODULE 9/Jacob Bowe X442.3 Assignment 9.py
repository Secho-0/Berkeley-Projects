import os

file_total = 0
for roots,dirs,files in os.walk('.'):
    for file in files:
        print(os.path.join(roots,file))
    file_count = len(files)
    file_total += file_count
    print("file count: ",file_count)
print('file total:', file_total)

##Sample : <img src="img_chania.jpg" alt="Flowers in Chania">
## re : ^(<img)(.*)(>)
import re
import urllib.request as urllibr

findimg = re.compile("(<img)(.*)(>)")

#open/read website
website = urllibr.urlopen('https://www.html.am/templates/downloads/bryantsmith/simplegallery/#./images/1.jpg')
html = str(website.read())
website.close()

imgs = findimg.findall(html)

for entry in imgs:
    for value in entry:
        print(value)
