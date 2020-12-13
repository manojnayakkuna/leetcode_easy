# -*- coding: utf-8 -*-
"""
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
Example 1: Input: area = 4
Output: [2,2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
Example 2: Input: area = 37
Output: [37,1]
Example 3: Input: area = 122122
Output: [427,286]
"""
# Traditional Approach - 33%
def constructRectangle(self, area: int) -> List[int]:
    for i in range(int(area**0.5), 0, -1):
        if area % i == 0:
            return [area//i, i]

#Traditional Approach - 24/52
def constructRectangle(area):
    left = 1
    right = area
    minleft = None
    minright = None
    while left <= area and right > 0:
        if left*right == area:
            if left >= right:
                if minleft is None and minright is None:
                    minleft = left
                    minright = right
                else:
                    if abs(right-left)<abs(minright-minleft):
                        minleft = left
                        minright = right
            left += 1
            right -= 1
        elif left * right > area:
            right -= 1
        elif left * right < area:
            left += 1
    return [minleft,minright]
return [[area // l, l] for l in range(int(area**0.5), 0, -1) if area % l == 0][0]