## Question 1 
dict = {'cherry':'1','apple':'2','banana':'3'}
keylist = []
for key in dict.keys():
    while key not in keylist:
        keylist.append(key)
#print(keylist)
keylist.sort()
#print(keylist)
for key in keylist:
    print(key + ':' + dict[key])
        
## Question 2 
a = [7,12,9,14,15,18,12]
b = [9,14,8,3,15,17,15]
big = []
ct = 0
while ct < len(a):
    big.append(max(a[ct],b[ct]))
    print(big)
    ct+= 1
## Question 3
ttl_chars = 0
file = open("Lorem.txt",'r')
linelens = []
while ttl_chars < 1001:
    linelen = len(file.readline())
    linelens.append(linelen)
    ttl_chars += linelen
    print("Read %d characters so far" % ttl_chars)
linelens.sort()
print("The longest line is: ", linelens[-1])

##Question 4
ttl_chars = 0
file = open("Lorem.txt",'r')
linelens = []
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
linelens.sort()
print("The longest line is: ", linelens[-1])

