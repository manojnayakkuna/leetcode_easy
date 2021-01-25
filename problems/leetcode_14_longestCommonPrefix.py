# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:48:50 2020

@author: manoj
"""
#Time Complexity = O(n^2)
def longestCommonPrefixBruteMethod(strs):
    if len(strs) <= 0:
        return ''
    
    cnt = 1
    loopInd = 'Y'
    strCompare = ''
    strEmptyCnt = 0
    while loopInd == 'Y':
        strCompare = strs[0][:cnt]
        print ('strCompare:',strCompare)
        for i in range(len(strs)):
            print ('strs[i][:cnt]:',strs[i][:cnt])
            if len(strs[i][:cnt]) > 0:
                if strCompare != strs[i][:cnt]:
                    loopInd = 'N'
                    break
            else:
                strEmptyCnt += 1
        if strEmptyCnt == len(strs):
            loopInd = 'N'
            break
        if loopInd == 'Y':
            cnt += 1
            strCompare = strs[0][:cnt]        
    if cnt == 1:
        return ''
    else:
        return strCompare[:-1]

def longestCommonPrefix(strs):
    result = ''
    if len(strs) <= 0:
        return result
    
    minLength = strs[0]
    for i in range(1,len(strs)):
        if len(strs[i]) < len(minLength):
            minLength = strs[i]
    
    if minLength == 0:
        return result
    else:
        cnt = 1
        while cnt <= len(minLength):
            compare = minLength[:cnt]
            for i in range(len(strs)):
                if compare != strs[i][:cnt]:
                    break
                else:
                    if i == len(strs)-1:
                        result = compare
            cnt += 1
        return result

Input1 = ["flower","flow","flight"]
Input2 = [""]
Input3 = ["a"]

print (longestCommonPrefix(Input1))

#minLength = list(map(lambda string: string, Input1))

#minLength = map(lambda string: string, Input1)
#minLength = list(minLength)

key=lambda x: len(x)
#print('length:',key(Input1))

#print (min(Input1,key=lambda x:len(x)))

res = ""
if not Input1:
    print (res)
for i in range(len(min(Input1,key=lambda x: len(x)))):
    if all(Input1[k][i] == Input1[k+1][i] for k in range(len(Input1)-1)):
        res += Input1[0][i]
    else:
        break
print (res)