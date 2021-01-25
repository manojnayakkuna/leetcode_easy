# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:51:55 2020

@author: manoj
"""
d = {}
list1 = [8,1,2,2,3]
for num,value in enumerate(sorted(list1)):
    if value not in d:
        d[value] = num

print (d)
print ([d[num] for num in list1])
print (sorted(list1))
print ([sorted(list1).index(i) for i in list1])

from collections import defaultdict
sl = sorted(list1, reverse=True)
print ('sl:', sl)
prev = 0
counts = defaultdict(lambda: 0)

for i in range(1, len(sl)):
    if sl[prev] != sl[i]:
        counts[sl[prev]] = len(sl) - prev - 1
        print ('counts:', counts)
    prev += 1

print ([counts[list1[i]] for i in range(len(list1))])