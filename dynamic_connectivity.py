#
# QuickFind/Union - Dynamic connectivity
#
import numpy

class QuickFind(object):
    def __init__(self, N):
        self.lst = list(range(N))
        print(self.lst)    

    def Find(self, p, q):
        print("Starting Find")
        if self.lst[p] == self.lst[q]:
            print("Math: "+p , q)

    def Union(self, p, q):
        print("Starting Union")
        pid = self.lst[p]
        qid = self.lst[q]
        for ind, x in enumerate(self.lst):
            if x == pid:
                self.lst[ind] = qid