# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:58:57 2020

@author: manoj
"""

#Below Examples Shows Various Ways Of splitting a string into a list

#Method 1: Using List Compression
def usingListCompr(num,n):
    #num = 1234567
    s = str(num)
    #s = s[::-1]
    s = [s[i:i+n] for i in range(0, len(s), n)]
    # print([s[idx:idx+2] for idx,val in enumerate(s) if idx%2 == 0])
    s = '.'.join(s)
    #return s[::-1]
    return s

def split_by_n(num, n):
    '''A generator to divide a sequence into chunks of n units.'''
    seq = str(num)
    while seq:
        yield seq[:n]
        seq = seq[n:]

def usingWhileExtraSpace(num,n):
    s = str(num)
    o = []
    while s:
        o.append(s[:n])
        s = s[n:]

def usingRecursion(num,n):
    s = str(num)
    if len(s) < n:
        return []
    else:
        return [s[:n]] + usingRecursion(s[n:], n)

def usingSlice(num,n):
    from more_itertools import sliced
    return list(sliced(str(num), n))
    
def usingRe(num,n):
    import re
    #Method 1
    #splitFreq = '.'*n
    #s = re.findall(splitFreq,str(num)) --- > Works for only even length num
    
    #Method 2
    #splitFreq += '?'
    #s = re.findall('...?',str(num))  #Deos Not Work
    
    #Method 3
    splitFreq = '.{1,'+str(n)+'}'
    s = re.findall(splitFreq,str(num))   # Works for all
    s = '.'.join(s)
    return s

def usingWrap(num,n):
    from textwrap import wrap
    s = str(num)
    return wrap(s, n)

def usingMapZip(num,n):
    s = str(num)
    return map(''.join, zip(*[iter(s)]*n))

def usingIterTools(num,s):
    import more_itertools as mit
    #import more_itertools_sliced
    s = str(num)
    ["".join(c) for c in mit.grouper(2, s)]
    ["".join(c) for c in mit.chunked(s, 2)]
    ["".join(c) for c in mit.windowed(s, 2, step=2)]
    ["".join(c) for c in  mit.split_after(s, lambda x: int(x) % 2 == 0)]

print(usingListCompr(1234567,3))
print(usingRe(1234567,3))