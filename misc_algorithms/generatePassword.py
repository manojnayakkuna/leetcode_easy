# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:20:24 2020

@author: manoj
"""

import secrets
#import random
def generatePassword(strList,passwordLength):
    strSelected = [secrets.choice(strList) for i in range(passwordLength)]
    return ''.join(strSelected)


strLists = ['1','12','21','11','22','2','123','132','321','111','222','333','1234','1111','2222','3333','4444','1243','1423','4123','4222','3222','1222','3222','3111','3112','4112']
print ('Password',generatePassword(strLists,7))