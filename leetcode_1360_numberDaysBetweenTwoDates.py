# -*- coding: utf-8 -*-
"""
Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
Example 1: Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2: Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
"""
# 81%
def daysBetweenDates(date1, date2):
    
    def isLeapYear(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
            else:
                return True
        return False
        
    date1Y, date1M, date1D = map(int,date1.split('-'))
    date2Y, date2M, date2D = map(int,date2.split('-'))
    leapYear    = [31,29,31,30,31,30,31,31,30,31,30,31]
    nonLeapYear = [31,28,31,30,31,30,31,31,30,31,30,31]
    T1, T2 = 0, 0
    if date1Y > date2Y:
        for i in range(date2Y, date1Y):
            T1 += 366 if (isLeapYear(i)) else 365
        T1 += sum(leapYear[:date1M-1])+date1D if (isLeapYear(date1Y)) else sum(nonLeapYear[:date1M-1])+date1D
        T2 = sum(leapYear[:date2M-1])+date2D if (isLeapYear(date2Y)) else sum(nonLeapYear[:date2M-1])+date2D
    else:
        T1 = sum(leapYear[:date1M-1])+date1D if (isLeapYear(date1Y)) else sum(nonLeapYear[:date1M-1])+date1D
        for i in range(date1Y, date2Y):
            T2 += 366 if (isLeapYear(i)) else 365
        T2 += sum(leapYear[:date2M-1])+date2D if (isLeapYear(date2Y)) else sum(nonLeapYear[:date2M-1])+date2D
    
    return abs(T1-T2)

# 50%
def daysBetweenDates1(date1, date2):
    def isleapyear(year):
        flag=False
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    flag=True
            else:
                flag=True
        return flag
    
    def totaldays(year,month,day):
        md=[31,28,31,30,31,30,31,31,30,31,30,31]
        total=0
        for i in range(1971,year):
            total+=366 if isleapyear(i) else 365
        return total+sum(md[:month-1])+day
    
    y1,m1,d1=map(int,date1.split("-"))
    y2,m2,d2=map(int,date2.split("-"))
    t1=totaldays(y1,m1,d1)
    t2=totaldays(y2,m2,d2)
    if isleapyear(y1) and m1>2:
        t1+=1
    if isleapyear(y2) and m2>2:
        t2+=1
    
    return abs(t1-t2)
