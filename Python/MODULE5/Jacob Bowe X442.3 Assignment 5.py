
## Question 1 
# Create a dictionary, and list for its keys
dict = {'cherry':'1','apple':'2','banana':'3'}
keylist = []

# Add Each Key to the keylist
for key in dict.keys():
    while key not in keylist:
        keylist.append(key)

#print(keylist)
keylist.sort()
#print(keylist)

# Automatically print the keyname + its value from the dictionary
for key in keylist:
    print(key + ':' + dict[key])


## Question 2 
# Setup two lists of numbers, an empty list for the largest of the two
a = [7,12,9,14,15,18,12]
b = [9,14,8,3,15,17,15]
big = []
ct = 0

# for the larger of the two numbers in the list (i.e 7 in list 'a' and 9 in list 'b') add the larger of the two (9) to the list 'big' 
# do this until we are at the end of list 'a'
while ct < len(a):
    big.append(max(a[ct],b[ct]))
    print(big)
    ct+= 1

    
## Question 3
ttl_chars = 0
file = open("MODULE5\Lorem.txt",'r')
linelens = []
# Open a textfile, read the lines until at least 1000 characters have been read
while ttl_chars < 1001:
    linelen = len(file.readline())
    linelens.append(linelen)
    ttl_chars += linelen
    print("Read %d characters so far" % ttl_chars)
# Sort line lengths and print longest line read
linelens.sort()
print("The longest line is: ", linelens[-1])

##Question 4

ttl_chars = 0
file = open("MODULE5\Lorem.txt",'r')
linelens = []
# Read first 1000 characters, unless the line starts with a '#'
for line in file:
    if ttl_chars > 1000:
        break
    if line.startswith('#'):
        print("Skipping a Line")
    else:
        linelen = len(line)
        linelens.append(linelen)
        ttl_chars += linelen
        print("Read %d Characters so far..." % ttl_chars)
        
# Sort line lengths and print longest
linelens.sort()
print("The longest line is: ", linelens[-1])

