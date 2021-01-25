# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:28:08 2020

@author: manoj
"""

#import pickle

def saveDict(dictToSave,filePath):
    with open(filePath,'wb') as file:
        pickle.dump(dictToSave,file)
        
def ReadDict(filePath):
    with open(filePath,'rb') as file:
        return pickle.load(file)
    
testDict = {'a':1,'b':2,'c':3}
saveDict(testDict,'testdict.pickle')

print(ReadDict('testdict.pickle'))