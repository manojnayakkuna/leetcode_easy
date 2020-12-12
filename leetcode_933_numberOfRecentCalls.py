# -*- coding: utf-8 -*-
"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:
RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]
Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
"""

#Easy but it times out for lastger value. Can be implemented with binary search logic
class RecentCounter:

    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:
        if len(self.stack) == 0:
            self.stack.append(t)
            return 1
        else:
            self.stack.append(t)
            lowRange = t - 3000
            counter = 0
            for i in range(len(self.stack)):
                if lowRange <= self.stack[i] <= t:
                    counter += 1
            return counter

#A bit tricky to understand but uses list index difference value to compare and capture the values
class RecentCounter1:

    def __init__(self):
        self.ls=[]
        self.low=0
        self.high=0

    def ping(self, t: int) -> int:
        self.ls.append(t)
        while True:
            if self.ls[self.low]>=t-3000:
                break
            else:
                self.low+=1
        self.high+=1
        return (self.high-self.low)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)