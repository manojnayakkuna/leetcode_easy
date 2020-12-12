# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 01:08:22 2020

@author: manoj
"""

# Definition for singly-linked list.
# Method 1: 4 Pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        cnt = 1
        oddPtr = None
        evenPtr = None
        while head is not None:
            print ('cnt:',cnt,'head.val:',head.val)
            if cnt % 2 == 0:
                newNode = ListNode(head.val)
                if evenPtr is None:
                    evenPtr = newNode
                    evenHead = evenPtr
                else:
                    evenPtr.next = newNode
                    evenPtr = evenPtr.next
            else:
                newNode =  ListNode(head.val)
                if oddPtr is None:
                    oddPtr = newNode
                    oddHead = oddPtr
                else:
                    oddPtr.next = newNode
                    oddPtr = oddPtr.next
            cnt = cnt + 1
            head = head.next
        
        oddPtr.next = evenHead
        
        return oddHead
    
#Method 2: 3 pointers
class Solution1:
    def oddEvenList1(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        curr = head.next
        even = head.next
        odd = head 

        while curr and curr.next:
            # put items in odd list
            odd.next = curr.next
            odd = odd.next

            # fix the even list
            curr.next = curr.next.next
            curr = curr.next
        odd.next = even
        return head

#Method 3: 2 pointer
class Solution2:
    def oddEvenList2(self, head: ListNode) -> ListNode:
        ## RC ##
        ## LOGIC : START WITH BASIC EVEN AND ODD POSITIONS, FOR NEXT ODD APPEND EVENS NEXT AND FOR NEXT EVEN APPEND ODDS NEXT ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        if(not head): return head
        odd = head
        even = head.next
        evenHead = even
        while(even and odd and even.next and odd.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head