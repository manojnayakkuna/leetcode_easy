# -*- coding: utf-8 -*-
"""
Created on Tue May 12 01:29:42 2020

@author: manoj
"""

def productSearch(products,searchWord):
    products.sort()
    pool = []
    for i in range(len(searchWord)):
        count = 0
        searchPool = []
        for product in products:
            if product[:i+1] == searchWord[:i+1]:
                if count < 3:
                    searchPool.append(product)
                    count = count + 1
                else:
                    break
        pool.append(searchPool)
    
    return pool

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print ('results:',productSearch(products,searchWord))

products = ["havana"]
searchWord = "havana"
print ('results:',productSearch(products,searchWord))

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
print ('results:',productSearch(products,searchWord))

products = ["havana"]
searchWord = "tatiana"
print ('results:',productSearch(products,searchWord))