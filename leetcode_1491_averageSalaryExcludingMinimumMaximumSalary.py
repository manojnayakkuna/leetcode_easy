# -*- coding: utf-8 -*-
"""
Given an array of unique integers salary where salary[i] is the salary of the employee i.
Return the average salary of employees excluding the minimum and maximum salary.
Example 1: Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500
Example 2: Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000)/1= 2000
Example 3: Input: salary = [6000,5000,4000,3000,2000,1000]
Output: 3500.00000
Example 4: Input: salary = [8000,9000,2000,3000,6000,1000]
Output: 4750.00000
"""
# 53%
def average(salary):
    return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)

def average1(salary):
    return sum(sorted(salary)[1:-1])/(len(salary)-2)

def average2(salary):
    newsal=sorted(salary)
    newsal.pop(0)
    newsal.pop(len(newsal)-1)
    avg=0.0
    for i in newsal:
        avg+=i
    avg=avg/len(newsal)
    return avg