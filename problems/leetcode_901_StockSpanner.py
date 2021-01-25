# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:21:09 2020

@author: manoj
"""

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        count = 1
        i = len(self.stack) - 2
        while i >= 0:
            if price >= self.stack[i]:
                count += 1
            else:
                break
            i = i - 1
        return count
    
class StockSpannerInternet:

    def __init__(self):
        self.price = []  # stores price of i'th day
        self.span = []  # stores span of i'th day
        self.day = -1  # count days

    def next(self, price: int) -> int:
        self.day += 1
        self.price.append(price)
        # try to find latest price which is greater than today's price
        last = self.day - 1  # start with yesterday
        while last > -1 and self.price[last] <= price:  # if price on particular day is lesser or equal
            last -= self.span[last]  # try using that days span
        self.span.append(self.day - last)
        return self.span[self.day]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)