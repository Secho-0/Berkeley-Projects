from Rectangle import Ulist as UL

print(UL)
myList = UL([0,2,4,6,8,10])
print(myList)   
myList.append(11)
print(myList)
myList.append(2)
print(myList)
myList.extend([0,1,3,5,11,9])
print(myList)
myList.extend([0,1,2,18,23])
print(myList)
myList = myList + 7
print(myList)
myList = myList + 13
print(myList)
myList = myList + '123'
print(myList)
myList = myList + [14,20,11]
print(myList)
input()