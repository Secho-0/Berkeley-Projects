
myvar = 'Python Programming'

# print P from first character in string
p1 = myvar[0]
print(p1)

# print rightmost index of P
p2 = myvar[myvar.rindex('P')]
print(p2)

# Split myvar by spaces into a list, print the first character of the first string in the new list
myvar = myvar.split(' ')
p3 = myvar[0][0]
print(p3)

# Return the length of a string, disguised as a number 
num = input('Input a number: ')
print(len(num))
