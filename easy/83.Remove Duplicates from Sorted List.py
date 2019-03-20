"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
    Input: 1->1->2
    Output: 1->2

Example 2:
    Input: 1->1->2->3->3
    Output: 1->2->3
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def deleteDuplicates(head):  # 28 ms, faster than 100%; 10.8 MB, less than 65.12%
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head
    current_node = head
    next_node = current_node.next
    while next_node:
        if next_node.val != current_node.val:
            current_node.next = next_node
            current_node = next_node
        next_node = next_node.next
    current_node.next = None
    return head


def deleteDuplicates2(head):
    iter = head
    while iter is not None and iter.next is not None:
        if iter.val == iter.next.val:
            iter.next = iter.next.next  # alternative idea ***
        else:
            iter = iter.next
    return head
