
# setup a tuple
mytup = (1,2,3,4)
print(mytup)

# turn tuple into a list
mytuplist = list(mytup)
print(mytuplist) 

# reverse the list
mytuplist.reverse()
print(mytuplist)

#store the newly reversed list as back as original tuple
mytup = tuple(mytuplist)
print(mytup)
#congrats your tuple is flipped
