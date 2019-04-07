"""
Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up:
    A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):  # 28 ms, faster than 54.46%
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head
    stack = []
    while head.next:
        stack.append(head)
        head = head.next
    curr = head
    while stack:
        curr.next = stack.pop()
        curr = curr.next
    curr.next = None
    return head


def reverseList2(head):  # 24 ms, faster than 91.22%, best solution from submissions.
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

