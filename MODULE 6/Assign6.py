#Question 1 
file = open("Lorem2.txt",'r')
totals = ()
def count_characters(file):
    char_count = 0
    char_total = 0
    word_count = []
    word_total = 0
    ct = 0

    for line in file:
        print(line)
#   Count characters
        char_count = len(line) + 1
        print(char_count,"Characters on this line")
        char_total += char_count
#  Count words
        word_count = line.split()
        print(len(word_count),"Words on this line")
        word_total += len(word_count)
# Count lines
        ct+=1
        print(ct, "Lines so far\n")
    return char_total, word_total, ct

totals = count_characters(file)
print(totals)
print("Total Characters: ",totals[0],
      "\nTotal Words: ",totals[1],
      "\nTotal Lines: ",totals[2])

#Question 2
# Am I allowed to be cheeky and use last modules list? :P
a = [7,12,9,14,15,18,12,58,70,32,54]
b = [9,14,8,3,15,17,15,70,98,54,31]

big = []
ct = 0
while ct < len(a):
    if a[ct] not in big:
        big.append(a[ct])
    if b[ct] not in big:
        big.append(b[ct])
    ct +=1
print(big)
#personal preference on bigs print
#big.sort()
#print(big)


#Question 3
fav_nums = [ 1, 2, 4, 5, 8, 10, 25, 50, 100]
print("Map Function List: ",list(map(lambda x:x+8,fav_nums)))

lst2 = [x+8 for x in fav_nums]
print("List Comprehension: ", lst2)

#Question 4
wl1 = ["double", "triple", "int", "quadruple"]
wl2 = ["double", "home run"]
wl3 = ["int", "double", "float"]

def count_lists(*lists):
    wlcount = {}
    for lst in lists:
        for word in lst:
            if word in wlcount:
                wlcount[word] +=1
            if word not in wlcount:
                wlcount[word] = 1
    return wlcount
print(count_lists(wl1,wl2,wl3))
