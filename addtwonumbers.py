'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        orig = ListNode(carry)
        res = orig
        rem = False
        while True:
            val = l1.val + l2.val + carry
            carry = val // 10
            val = val % 10
            # print(l1.val, l2.val, val, carry)
            res.val = val
            
            if l1.next is None or l2.next is None:
                rem = True
                break
            else:
                res.next = ListNode(0)
                res = res.next 
                l1 = l1.next
                l2 = l2.next
        if rem:
            # print("rem")
            remaining = l1 if l1.next is not None else l2
            
            remaining = remaining.next
            while remaining is not None or carry > 0:
                res.next = ListNode(0)
                res = res.next
                val = carry + remaining.val if remaining is not None else carry
                carry = val // 10
                val = val % 10
                res.val = val
                if remaining is not None and remaining.next is not None:
                    remaining = remaining.next
                else:
                    break
        if carry > 0:
            res.next = ListNode(carry)
        # res.val = carry
        return orig

