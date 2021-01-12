# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:08:28 2020

@author: manoj
"""
import collections

def relativeSortArray(arr1, arr2):
    digitsArr1 = collections.Counter(arr1)
    #for i in range(len(arr1)):
    #    digitsArr1[arr1[i]] = digitsArr1[arr1[i]] + 1
    #setNew = set(arr1)
    #print ('setNew:', setNew)
    string = ''
    for j in range(len(arr2)):
        if digitsArr1[arr2[j]] > 0:
            newstr = str(arr2[j])+' '
            string = string + ' ' + digitsArr1[arr2[j]]*newstr
            arr1[:] = [x for x in arr1 if x != arr2[j]]
            print ('arr1:', arr1)
            #print ('arr2[j]:', arr2[j])
            #arr1 = lambda x: for x in arr1 if x == arr2[j]
            #arr1.remove(arr2[j])
    #string = list(string)
    string = string.split()
    arr1.sort()
    string = string + arr1
    return [int(x) for x in string]

def internetMethod1(arr1,arr2):
    dic = collections.Counter(arr1)
    ans = []
    
    for x in arr2:
        ans += [x]*dic[x]
        del dic[x]
    
    for x in sorted(dic):
        for n in range(dic[x]):
            ans.append(x)
   
    return ans

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
#print(relativeSortArray(arr1,arr2))

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(relativeSortArray(arr1,arr2))
    
            