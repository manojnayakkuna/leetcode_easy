# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:55:25 2020

@author: manoj
"""

def listIterCustom(myList,item):
    indices = []
    for i in range(len(myList)):
        print ('i:',i)
        if myList[i] == item:
            print ('inside if i:',i, ' myList[i]:', myList[i])
            indices.append([i])
            print ('indices:',indices)
        elif isinstance(myList[i],list):
            print ('myList[i]:', myList[i])
            for index in listIterCustom(myList[i],item):
                print ('index:', index, 'i:',i)
                indices.append([i]+index)
                print ('indices:', indices)
    return indices

def listIter(myList,item,indices):
#def listIter(myList,item):
    #indices = []
    for i in range(len(myList)):
        #print ('i:',i)
        if myList[i] == item:
            indices.append([i]+[myList.index(myList[i])])
        elif isinstance(myList[i],list):
            print ('myList[i]:', myList[i])
            #indices.append([i]+[myList.index(myList[i])])
            print ('indices:', indices)
            print ('myList.index(myList[i]):', myList.index(myList[i]))
            indices.append([i]+[myList.index(myList[i])])
            print ('indices:', indices)
            listIter(myList[i], item, indices)
            #for index in listIter(myList[i],item):
            #    print ('index:', index)
            #    indices.append([i]+index)
            
    return indices
    
indices = []
item = 2
myList = [[[1,2,3],2,[3,4,2]],[6,1,2],2]
indices = listIterCustom(myList,item)
#listIter(myList,item,indices)
print ('indices:',indices)