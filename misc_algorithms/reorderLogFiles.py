# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:43:46 2020

@author: manoj
"""

def reorderLogFiles(arr,n):
    if n <= 0:
        return []
    
    letList = []
    digList = []
    for i in range(n):
        #if arr[i][:3] == 'let':
        if arr[i].split()[1].isdigit():
            digList.append(arr[i])
        else:
            letList.append(arr[i].split())
    
    for i in range(len(letList)):
        for j in range(len(letList)):
            if j != i:
                if letList[j][1] > letList[i][1]:
                    temp = letList[j]
                    letList[j] = letList[i]
                    letList[i] = temp
    
    for i in range(len(letList)):
        letList[i] = " ".join(letList[i])
        
        """    
    for i in range(len(digList)):
        for j in range(len(digList)):
            if j != i:
                if digList[j][1] < digList[i][1]:
                    temp = digList[j]
                    digList[j] = digList[i]
                    digList[i] = temp   
    for i in range(len(digList)):
        digList[i] = " ".join(digList[i])
        """

    return  letList + digList

def internetMethod(logs,n):
    if n <= 0:
        return []
    
    letList = []
    digList = []
    for i in range(n):
        if logs[i].split()[1].isdigit():
            digList.append(logs[i])
        else:
            letList.append(logs[i].split())
    
    #print ('original letList:', letList)
    letList.sort(key = lambda logs: logs[0])
    #print ('after 1st sort letList:', letList)
    letList.sort(key = lambda logs: logs[1:])
    #print ('after 2nd sort letList:', letList)

    for i in range(len(letList)):
        letList[i] = " ".join(letList[i])

    return  letList + digList

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
result = reorderLogFiles(logs,len(logs))
print ('customMethod result  :', result)
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
result = internetMethod(logs,len(logs))
print ('internetMethod result:', result)

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
result = reorderLogFiles(logs,len(logs))
print ('customMethod result  :', result)
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
result = internetMethod(logs,len(logs))
print ('internetMethod result:', result)

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
result = reorderLogFiles(logs,len(logs))
print ('customMethod result  :', result)
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
result = internetMethod(logs,len(logs))
print ('internetMethod result:', result)