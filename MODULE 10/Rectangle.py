class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def rect_perim(self):
        return (2*self.length) + (2*self.width)
    def rect_area(self):
        return self.length * self.width

from collections import UserList
class Ulist(UserList):
    def __init__(self,other):
        super().__init__(other) 
    def append(self,other):
        if other not in self.data:
            self.insert(len(self),other)
        else:
            pass
    def extend(self,others):
        for o in others:
            self.append(o)
    def __add__(self, other):
        if isinstance(other, int or str):
                if other not in self.data:
                    return self.__class__(self.data + [other])
                else:
                    pass
        elif isinstance(other, list):
            n = []
            for o in other:
                if o not in self.data:
                    n.append(o)
                    print(n)
                else:
                    pass
            return self.__class__(self.data + n)
        return self.__class__(self.data + [other])
