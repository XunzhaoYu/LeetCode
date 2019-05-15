"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        # 68 ms, faster than 99.79%. The best one is 60 ms (recursive solution)
        res, carry = l2, 0
        while l1:
            carry, mode = divmod(l1.val + l2.val + carry, 10)
            l2.val = mode
            if not l2.next:
                if l1.next:
                    l2.next = l1.next
                    l2 = l2.next
                    break
                elif carry:
                    l2.next = ListNode(carry)
                return res
            l1, l2 = l1.next, l2.next
        while True:
            carry, mode = divmod(l2.val + carry, 10)
            l2.val = mode
            if l2.next:
                l2 = l2.next
                continue
            elif carry:
                l2.next = ListNode(carry)
            return res
