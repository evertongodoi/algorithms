import numpy
from dynamic_connectivity import QuickFind

file = open('tinyUF.txt', 'r') 

entries = int(file.readline())
print("\nNumber of entries: {}".format(entries))

implementation = QuickFind(entries)