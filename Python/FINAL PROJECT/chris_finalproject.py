import os
from collections import Counter

# set Directory
# 'C:\\Users\\Valued Customer\\Google Drive\\School\\ELENGX442.3 - 013 - INTRODUCTION TO PYTHON\\FINAL PROJECT\\finalproject'
dir = "B:\Personal\School\ELENGX442.3 - 013 - INTRODUCTION TO PYTHON\FINAL PROJECT\\finalproject"
os.chdir(dir)
dirlist = os.listdir('.')

# get file list in directorys, split the extensions
dirlist_split = [ os.path.splitext(f) for f in dirlist]
dirlist_split = sorted(dirlist_split, key=lambda x: x[1])


# get file sizes
file_sizes = {}
for entry in dirlist_split:
    (x, y) = entry
    filename = x + y
    filesize = os.path.getsize(filename)
    file_sizes.setdefault(y,[]).append(filesize)
    #print ('Filename: %-30s \nSize: %-6d bytes' % (filename, filesize))
    
print('-'*30)

# get a count on the extensions in the directory
ext_count = Counter(file[1] for file in dirlist_split)
for a in ext_count.items():
    (x, y) = a
    if (x == ''):
        ext = 'None'
    else: 
        ext = x
    print('Extension: %-6s Count: %-6d' % (ext, y))
for ext,lst in file_sizes.items():
    lst.sort()
    avg = sum(lst)/len(lst)
    mini = min(lst) ## lst[0]
    maxi = max(lst) ## lst[-1]
    print('-'*30,'\n',ext,'\nMinimum Size: %-10d \nMaximium Size: %-10d \nAverage Size: %-10d' % (mini,maxi,avg))
    
print('-'*30)


