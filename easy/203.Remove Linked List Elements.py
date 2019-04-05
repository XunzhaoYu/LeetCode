"""
Remove all elements from a linked list of integers that have value val.

Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def removeElements(head, val):  # 64 ms, faster than 66.16%, same to the best from submissions
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if head:
            prev, curr = head, head.next
            while curr:
                if curr.val == val:
                    prev.next = curr.next
                    del curr
                    curr = prev.next
                else:
                    prev, curr = curr, curr.next
        return head

